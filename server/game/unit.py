from hittableObject import *

class Unit(HittableObject):
    """
    Any object that is owned by a player and can move inherits from this class.
    This class handles functions related to attacking and moving.
    """
    def __init__(self, game, x, y, z, owner, type):
        HittableObject.__init__(self, game, x, y, z, type)
        #TODO: fix
        self.owner = owner

    def toList(self):
        list = HittableObject.toList(self)
        #TODO: fix
        #list.extend([self.moves])
        return list

    def nextTurn(self):
        HittableObject.nextTurn(self)

    def move(self, targetX, targetY):
        return True

    def attack(self, targetX, targetY):
        return True



