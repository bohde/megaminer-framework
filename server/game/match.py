from base import *
from matchUtils import *

from gameObject import *
from unitType import *
from buildingType import *
from mappableObject import *
from hittableObject import *
from building import *
from unit import *
from portal import *
from config.config import *
from collections import defaultdict
from sexpr.sexpr import *
import bz2
import os

def loadClassDefaults(cfgFile = "config/defaults.cfg"):
    cfg = readConfig(cfgFile)
    for className in cfg.keys():
        for attr in cfg[className]:
            setattr(eval(className), attr, cfg[className][attr])

class Match(DefaultGameWorld):
    def __init__(self, id):
        self.id = int(id)
        DefaultGameWorld.__init__(self, 10, 10)
        self.unitcfg = "config/unitSet.cfg"
        self.buildingcfg = "config/buildingSet.cfg"
        self.loadUnitSet(self.unitcfg)
        self.loadBuildingSet(self.buildingcfg)
        if (not os.path.exists("logs/")):
            os.mkdir("logs/")
        if (os.path.exists(self.logPath())):
            os.remove(self.logPath())

    def addPlayer(self, connection, type="player"):
        if (len(self.players) >= 2 and cmp(type, "player") == 0):
            return "Game is full"
        if (cmp(type, "player") == 0):
            self.players.append(connection)
        elif (cmp(type, "spectator") == 0):
            self.spectators.append(connection)
        self.sendIdent()
        return True

    def sendIdent(self):
        #Tells everybody who is in the game
        for p in self.players:
            msg = self.identList(p)
            p.writeSExpr(msg)
        msg = self.identList()
        for s in self.spectators:
            s.writeSExpr(msg)
    
    def identList(self, tailoredTo=None):
        #Generates the ident message
        #(ident (player, player) (spectator, spectator, ...) playerNum)
        #playerNum is 0 or 1 if you are player 0 or 1.
        #otherwise, playerNum is -1.
        #"You" is defined as the connection that is referred to by
        #  the tailoredTo Parameter
        msg = ['ident', [], []]
        for p in self.players:
            msg[1].append(p.user)
        for s in self.spectators:
            msg[2].append(s.user)
        playerNum = -1
        if len(self.players) >= 1 and self.players[0] == tailoredTo:
            playerNum = 0
        if len(self.players) >= 2 and self.players[1] == tailoredTo:
            playerNum = 1
        msg.append(playerNum)
        return msg

    def removePlayer(self, connection):
        if (cmp(connection.type, "player") == 0):
            self.players.remove(connection)
        else:
            self.spectators.remove(connection)
        self.sendIdent()
        if self.winner is None and \
           self.turn is not None and \
           len(self.players) == 1:
            self.declareWinner(self.players[0])

    def start(self):
        if len(self.players) < 2:
            return "Game is not full"
        if (self.winner is not None or self.turn is not None):
            return "Game has already begun"
        self.organizeTechTree()
        basicMapGeneration(self)
        for player in self.players:
            player.gold = [0, 0, 0]
        self.turnNum = -1
        self.nextTurn()
        return True

    def nextTurn(self):
        with self.turnLock:
            self.turnNum += 1
            if (self.turn == self.players[0]):
                self.turn = self.players[1]
            else:
                self.turn = self.players[0]
            self.dealHungerDamage()
            for obj in self.objects.values():
                obj.nextTurn()

            self.writeToLog()
            self.sendChanged(self.spectators)
            self.checkWinner()
            if self.winner is None:
                self.sendStatus(self.players)
   
            for obj in self.objects.values():
                obj.changed = False
            self.animations = ["animations"]

    def checkWinner(self):
        for p in self.players:
            p.hasBuilding = False
        for obj in self.objects.values():
            if (isinstance(obj, Building)):
                obj.owner.hasBuilding = True
        if (self.players[0].hasBuilding == False):
            self.declareWinner(self.players[1])
        if (self.players[1].hasBuilding == False):
            self.declareWinner(self.players[0])
        if (self.turnNum >= self.turnLimit):
            if (self.netWorth(self.players[0]) > \
              self.netWorth(self.players[1])):
                self.declareWinner(self.players[0])
            else:
                self.declareWinner(self.players[1])

    def netWorth(self, player):
        value = 0
        for obj in self.objects.values():
            if (hasattr(obj, "owner")):
                if (obj.owner == player):
                    value += obj.type.effPrice(obj.level)
        return value
    
    def declareWinner(self, winner):
        self.winner = winner
        self.turn = None
        winnerIndex = 1
        if winner == self.players[0]:
            winnerIndex = 0
        msg = ["game-over", self.id, self.winner.user, winnerIndex]
        log = open(self.logPath(), "a")
        log.write(sexpr2str(msg))
        log.write('\n')
        log.close()
        log = open(self.logPath(), "r")
        bzlog = bz2.BZ2File(self.logPath()+".bz2", "w")
        bzlog.write(log.read())
        log.close()
        os.remove(self.logPath())
        for p in self.players:
            p.writeSExpr(msg)
        for p in self.spectators:
            p.writeSExpr(msg)

    def logPath(self):
        return "logs/" + str(self.id) + ".gamelog"

    def writeToLog(self):
        log = open(self.logPath(), "a")
        log.write(sexpr2str(self.status(False)))
        log.write('\n')
        log.write(sexpr2str(self.animations))
        log.write('\n')
    
    @requireReferences(Building, UnitType)
    def train(self, buildingID, typeID):
        return self.objects[buildingID].train(self.objects[typeID])

    @requireReferences(Unit)
    def attack(self, unitID, x, y):
        return self.objects[unitID].attack(x, y)

    @requireReferences(Unit)
    def move(self, unitID, x, y):
        return self.objects[unitID].move(x, y)

    @requireReferences(Unit)
    def paint(self, unitID, x, y):
        return self.objects[unitID].paint(x, y)

    @requireReferences(Unit, None, None, None)
    def build(self, unitID, x, y, typeID):
        return self.objects[unitID].build(x, y, self.objects.get(typeID,None))

    @requireReferences(Building)
    def cancel(self, buildingID):
        return self.objects[buildingID].cancel()

    @requireReferences(Unit)
    def warp(self, unitID):
        return self.objects[unitID].warp()

    def sendStatus(self, players):
        for i in players:
            i.writeSExpr(self.status())
            i.writeSExpr(self.animations)

    def sendChanged(self, players):
        """
        An alternative to sendStatus, where objects are only sent if they
        have changed since last turn.
        """
        for i in players:
            i.writeSExpr(self.status(False))
            i.writeSExpr(self.animations)

    def status(self, fullList = True):
        if (fullList):
            msg = ["status"]
        else:
            msg = ["changed"]

        msg.append(["game", self.turnNum, self.players[0].gold,
                    self.players[1].gold, self.periods[0].area.max_x,
                     self.periods[0].area.max_y, self.hungerDamage])
        typeLists = defaultdict(list)
        for obj in self.objects.values():
            if (fullList == True or obj.changed == True):
                typeLists[obj.__class__].append(obj)
        for type in typeLists.keys():
            if (len(typeLists[type]) > 0):
                msg.append([type.__name__] +
                           [j.toList() for j in typeLists[type]])
        return msg

    def loadUnitSet(self, cfgfile):
        unitConfig = readConfig(cfgfile)
        for name in unitConfig.keys():
            newType = UnitType(self)
            newType.name = name
            for attribute in unitConfig[name].keys():
                setattr(newType, attribute, unitConfig[name][attribute])
            self.addObject(newType)

    def loadBuildingSet(self, cfgfile):
        cfgDict = readConfig(cfgfile)
        for name in cfgDict.keys():
            newType = BuildingType(self)
            newType.name = name
            for attribute in cfgDict[name].keys():
                setattr(newType, attribute, cfgDict[name][attribute])
            self.addObject(newType)

    def organizeTechTree(self):
        """
        Pre: All unit and building types must be loaded.
        Post: Unit types and building types with their trainedBy or 
              builtBy attributes set to string names will have these values
              converted to the corresponding objects.  All others will have
              these attributes set to None.
              This function allows the tech tree to be set in the config files
        """
        for obj in self.objects.values():
            if (isinstance(obj, BuildingType)):
                obj.builtBy = self.getType(obj.builtBy)
            if (isinstance(obj, UnitType)):
                obj.trainedBy = self.getType(obj.trainedBy)

    def getBuilding(self, x, y, z):
        for obj in self.periods[z].area[(x,y)]:
            if isinstance(obj, Building):
                return obj
        return None

    def getPortal(self, x, y, z):
        for obj in self.periods[z].area[(x,y)]:
            if isinstance(obj, Portal):
                return obj
        return None

    def getTerrain(self, x, y, z):
        for obj in self.periods[z].area[(x,y)]:
            if isinstance(obj, Terrain):
                return obj
        return None

    def getEnemies(self, x, y, z):
        """
        Returns a list of enemies (to the current player) at the given
          location
        """
        enemies = []
        for obj in self.periods[z].area[(x,y)]:
            if (isinstance(obj, Building) or isinstance(obj, Unit)):
                if (obj.owner != self.turn):
                    enemies.append(obj)
        return enemies

    def getType(self, name):
        """
        Pre: name is a string
        Post: Returns the unit or building type with that name, or None
        """
        for obj in self.objects.values():
            if (hasattr(obj, "name")):
                if (cmp(obj.name, name) == 0):
                    return obj
        return None

    def dealHungerDamage(self):
        totalHunger = [0, 0, 0]

        for obj in self.objects.values():
            if (isinstance(obj, Building)):
                if (obj.owner == self.turn and obj.complete):
                    totalHunger[obj.z] -= int(obj.type.food * \
                                          obj.type.foodExp**obj.level)
            if (isinstance(obj, Unit)):
                if (obj.owner == self.turn):
                    totalHunger[obj.z] += obj.type.hunger

        for z in xrange(3):
            totalHunger[z] *= self.hungerDamage
            if totalHunger[z] > 0:
                if self.turn == self.players[0]:
                    curPlayer = 0
                else:
                    curPlayer = 1
                self.animations += [["hungerDamage", curPlayer, z,
                                     totalHunger[z]]]
                
        for obj in self.objects.values():
            if (isinstance(obj, Unit)):
                if (obj.owner == self.turn):
                    obj.takeDamage(max(0,totalHunger[obj.z]), True, True)

    def chat(self, player, message):
        for i in self.players:
            i.writeSExpr(['says', player.user, message])
        return True


loadClassDefaults()

