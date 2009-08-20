from base import *
from matchUtils import *

from gameObject import *
from unitType import *
from buildingType import *
from mappableObject import *
from hittableObject import *
from unit import *
from building import *
from portal import *
from config.config import *

class Match:
    world = DefaultGameWorld

    def __init__(self, id):
        self.id = int(id)
        self.nextid = 0
        self.maxid = 2147483600
        self.players = []
        self.turn = None #the player whose turn it is;
                         #None before and after the game.
        self.winner = None #the player who won the game;
                           #None before and during the game 
        self.objects = dict() #key: object's id
                              #value: instance of the object
        self.turnNum = 0
        self.animations = []

    def addPlayer(self, player):
        if len(self.players) >= 2:
            return "Game is full"
        self.players.append(player)
        return True

    def start(self):
        if len(self.players) < 2:
            return "Game is not full"
        self.sendStatus(self.players)
        self.turn = self.players[0]
        return True
    
    @requireReferences(Building)
    def train(self, buildingID, typeID):
        return self.objects(buildingID).train(self.objects(typeID))

    @requireReferences(Unit)
    def attack(self, unitID, x, y):
        return self.objects(unitID).attack(x, y)

    @requireReferences(Unit)
    def move(self, unitID, x, y):
        return self.objects(unitID).move(x, y)

    @requireReferences(Unit)
    def paint(self, unitID, x, y):
        return self.objects(unitID).paint(x, y)

    @requireReferences(Unit, BuildingType)
    def build(self, unitID, typeID, x, y):
        return self.objects(unitID).build(self.objects(typeID),x, y)

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
        list = ["status"]
        list.append(["game", self.turnNum])
        for i in players:
            i.writeSExpr(list)

    def addObject(self, newObject):
        self.animations += [["add", newObject.id]]
        self.objects[newObject.id] = newObject

    def loadUnitSet(self, cfgfile):
        cfgfile = "unitSet.cfg"
        unitConfig = readConfig(cfgfile)
        for name in unitConfig.keys():
            pass #TODO

    def loadBuildingSet(self, cfgfile):
        cfgfile = "buildingSet.cfg"
        buildingConfig = readConfig(cfgfile)
        #TODO
