from mappableObject import *

class HittableObject(MappableObject):
    """
    Any object that is destructible or targetable with weapons is an
    instance of this class.  This class contains any functions that
    are solely related to health, damage, or healing.
    """
    myType = "HittableObject"
    def __init__(self, game, x, y, z, type):
        MappableObject.__init__(self, game, x, y, z)
        #TODO: Fix

    def nextTurn(self):
        MappableObject.nextTurn(self)

    def toList(self):
        list = MappableObject.toList(self)
        #TODO: Fix
        #list.extend([self.hp])
        return list

    def isDestroyed(self):
        destroyed = False
        if (self.hp <= 0):
            destroyed = True
        return destroyed

    def takeDamage(self, damage):
        self.hp -= damage
        if (self.hp > self.maxHP * self.overheal):
            self.hp = self.maxHP * self.overheal

