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

class Match(DefaultGameWorld):
    def __init__(self, id):
        self.id = int(id)
        DefaultGameWorld.__init__(self, 10, 10)
        self.unitcfg = "config/unitSet.cfg"
        self.buildingcfg = "config/buildingSet.cfg"
        self.loadUnitSet(self.unitcfg)
        self.loadBuildingSet(self.buildingcfg)

    def addPlayer(self, player):
        if len(self.players) >= 2:
            return "Game is full"
        self.players.append(player)
        return True

    def start(self):
        if len(self.players) < 2:
            return "Game is not full"
        if (self.winner is not None or self.turn is not None):
            return "Game has already begun"
        self.turn = self.players[0]
        self.organizeTechTree()
        for player in self.players:
            player.gold = 0
        self.sendStatus(self.players)
        return True

    def nextTurn(self):
        self.turnNum += 1
        if (self.turn == self.players[0]):
            self.turn = self.players[1]
        else:
            self.turn = self.players[0]
        self.dealHungerDamage()
        for obj in self.objects.values():
            obj.nextTurn()
        self.sendStatus(self.players)
        self.writeToLog()
        self.animations = []

    def writeToLog(self):
        pass
    
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

    @requireReferences(Unit, None, None, BuildingType)
    def build(self, unitID, x, y, typeID):
        return self.objects[unitID].build(x, y, self.objects[typeID])

    @requireReferences(Building)
    def cancel(self, buildingID):
        return self.objects[buildingID].cancel()

    def sendMap(self, players):
        pass #TODO

    def sendIdent(self, players):
        if len(self.players) < 2:
            return False
        list = []
        for i in self.players:
            list += [[i.ID, i.user, i.screenName, i.type]]
        for i in players:
            i.writeSExpr(['ident', list, self.log.id])

    def sendStatus(self, players):
        msg = ["status"]
        msg.append(["game", self.turnNum])
        typeLists = defaultdict(list)
        for obj in self.objects.values():
            typeLists[obj.__class__].append(obj)
        for type in typeLists.keys():
            msg.append([type.__name__]+[j.toList() for j in typeLists[type]])
        for i in players:
            i.writeSExpr(msg)

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
                if (hasattr(obj, "builtBy")):
                    obj.builtBy = self.getType(obj.builtBy)
                else:
                    obj.builtBy = None
            if (isinstance(obj, UnitType)):
                if (hasattr(obj, "trainedBy")):
                    obj.trainedBy = self.getType(obj.trainedBy)
                else:
                    obj.trainedBy = None


    def getBuilding(self, x, y, z):
        for obj in self.periods[z].area[(x,y)]:
            if isinstance(obj, Building):
                return obj
        return None

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
                    totalHunger[obj.z] -= obj.type.food
            if (isinstance(obj, Unit)):
                if (obj.owner == self.turn):
                    totalHunger[obj.z] += obj.type.hunger
        for obj in self.objects.values():
            if (isinstance(obj, Unit)):
                if (obj.owner == self.turn):
                    obj.takeDamage(max(0,totalHunger[obj.z]), True)
