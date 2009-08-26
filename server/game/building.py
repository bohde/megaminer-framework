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
        if (self.game.turn is None):
            #buildings placed before the start of the game are complete
            self.complete = True
            self.hp = type.hp
        else:
            self.complete = False
            self.hp = 0
            self.beBuilt()

    def nextTurn(self):
        HittableObject.nextTurn(self)
        if (self.training is not None):
            if (self.game.turn == self.owner):
                self.progress += 1
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
        self.hp += math.ceil(self.type.hp * (1.0 / self.type.buildTime))
        self.hp = int(min(self.hp, self.type.hp))
        if (self.hp == self.type.hp):
            self.complete = True

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
        self.training = newUnitType
        self.progress = 0
        return True

from unit import *

