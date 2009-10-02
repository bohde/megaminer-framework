from mappableObject import *

class HittableObject(MappableObject):
    """
    Any object that is destructible or targetable with weapons is an
    instance of this class.  This class contains any functions that
    are solely related to health, damage, or healing.
    """
    myType = "HittableObject"
    def __init__(self, game, x, y, maxHP, overheal):
        MappableObject.__init__(self, game, x, y)
        self.maxHP = maxHP
        self.hp = maxHP
        self.overheal = overheal

    def nextTurn(self):
        MappableObject.nextTurn(self)

    def toList(self):
        list = MappableObject.toList(self)
        list.extend([self.hp, int(self.maxHP*self.overheal)])
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

