from mappableObject import *

class HittableObject(MappableObject):
    """
    Any object that is destructible or targetable with weapons is an
    instance of this class.  This class contains any functions that
    are solely related to health, damage, or healing.
    """
    myType = "HittableObject"
    def __init__(self, game, x, y, z, type, level):
        MappableObject.__init__(self, game, x, y, z)
        self.type = type
        self.level = level

    def nextTurn(self):
        MappableObject.nextTurn(self)

    def toList(self):
        list = MappableObject.toList(self)
        list.extend([self.hp])
        return list

    def isDestroyed(self):
        destroyed = False
        if (self.hp <= 0):
            destroyed = True
        return destroyed

    def takeDamage(self, damage, ignoreArmor=False):
        if (ignoreArmor):
            dmgTaken = int(damage)
        else:
            dmgTaken = max(damage - self.type.effArmor(self.level), 1)
        self.hp -= dmgTaken
        if (dmgTaken != 0):
            self.changed
            self.game.animations += [["hurt", self.id, self.hp]]
        if (self.isDestroyed()):
            self.game.removeObject(self)

