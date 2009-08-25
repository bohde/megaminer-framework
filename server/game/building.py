from hittableObject import *
import math

class Building(HittableObject):
    def __init__(self, game, x, y, z, owner, type):
        HittableObject.__init__(self, game, x, y, z, type)
        self.type = type
        self.complete = False
        self.hp = 0
        self.beBuilt()

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
