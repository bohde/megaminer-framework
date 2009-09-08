from hittableObject import *
#This include has been moved to the end of 
#the file to avoid recursive imports
#from unit import *
import math

class Building(HittableObject):
    def __init__(self, game, x, y, z, owner, type):
        HittableObject.__init__(self, game, x, y, z, type)
        self.type = type
        self.training = None #The type of unit in progress, or None
        self.progress = 0 #The number of turns spent training
        self.owner = owner
        self.linked = False #True if this building also exists in a future era
        self.complete = False
        self.level = 1
        if (self.game.turn is None):
            #buildings placed before the start of the game are complete
            self.bringToCompletion()
        else:
            self.hp = 0
            self.beBuilt()

    def toList(self):
        list = HittableObject.toList(self)
        if (self.training is not None):
            inTraining = self.training.id
        else:
            inTraining = -1
        ownerIndex = self.game.players.index(self.owner)
        list.extend([self.level, self.type.id, ownerIndex, inTraining, 
                     self.progress, 1 * self.linked, 1 * self.complete])
        return list


    def bringToCompletion(self):
        if (not self.complete):
            self.complete = True
            self.hp = self.type.hp
            if (self.z < 2):
                newBuilding = Building(self.game, self.x, self.y, self.z + 1,\
                                   self.owner, self.type)
                self.game.addObject(newBuilding)
                newBuilding.bringToCompletion()
                self.linked = True

    def removeFromMap(self):
        if (self.z > 0):
            pastSelf = self.game.getBuilding(self.x, self.y, self.z-1)
            if (pastSelf is not None):
                pastSelf.linked = False
        if (self.linked):
            futureSelf = self.game.getBuilding(self.x, self.y, self.z+1)
            self.game.removeObject(futureSelf)
        HittableObject.removeFromMap(self)

    def nextTurn(self):
        HittableObject.nextTurn(self)
        if (self.training is not None):
            if (self.game.turn == self.owner):
                self.progress += 1
                self.changed = True
            if (self.progress >= self.training.trainTime):
                newUnit = Unit(self.game, self.x, self.y, self.z, \
                               self.owner, self.training)
                self.game.addObject(newUnit)
                self.training = None
                self.progress = 0

    def beBuilt(self):
        """
        Increases this building's hp based on the amount of time required to
        build it.
        """
        if (self.complete):
            return str(self.id) + " is already complete"
        self.hp += math.ceil(self.type.hp*(1.0 / self.type.buildTime[self.z]))
        self.hp = int(min(self.hp, self.type.hp))
        self.changed = True
        if (self.hp == self.type.hp):
            self.bringToCompletion()

    def train(self, newUnitType):
        """
        Begin training the desired unit type
        """
        if (not self.game.turn == self.owner):
            return str(self.id) + " is not your building"
        if (newUnitType.trainedBy != self.type):
            return str(self.id) + " can not train that type"
        if (self.training is not None):
            return str(self.id) + " is already training a unit"
        if (self.owner.gold < newUnitType.price):
            return "You can not afford to train this unit"
        if (not self.complete):
            return str(self.id) + " can not train until completed"
        self.game.animations += [["train", self.id, newUnitType.id]]
        self.training = newUnitType
        self.progress = 0
        self.owner.gold -= newUnitType.price
        self.changed = True
        return True

    def cancel(self):
        if (not self.game.turn == self.owner):
            return str(self.id) + " is not your building"
        if (self.complete):
            return str(self.id) + " is complete and can not be canceled."
        self.owner.gold += self.type.price
        self.game.removeObject(self)
        return True

from unit import *

