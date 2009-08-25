from hittableObject import *

class Unit(HittableObject):
    """
    Any object that is owned by a player and can move inherits from this class.
    This class handles functions related to attacking and moving.
    """
    def __init__(self, game, x, y, z, owner, type):
        HittableObject.__init__(self, game, x, y, z, type)
        self.hp = type.hp
        self.actions = 0
        self.owner = owner
        self.type = type

    def toList(self):
        list = HittableObject.toList(self)
        #TODO: fix
        #list.extend([self.moves])
        return list

    def nextTurn(self):
        HittableObject.nextTurn(self)
        self.actions = self.type.actions

    def move(self, targetX, targetY):
        return True

    def attack(self, targetX, targetY):
        if (not self.owner == self.game.turn):
            return str(self.id) + " does not belong to you"
        if (self.actions < 1):
            return str(self.id) + " is out of actions"
        for target in self.game.world.periods[self.z].area[(targetX, targetY)]:
            target.takeDamage(self.type.damage)
        self.actions -= 1
        return True



