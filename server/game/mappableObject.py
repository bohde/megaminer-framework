from gameObject import *

class MappableObject(GameObject):
    """
    All objects that are associated with a single x, y location will
    inherit from this class.
    """

    def __init__(self, game, x, y, z):
        GameObject.__init__(self, game)
        self.x = x
        self.y = y
        self.z = z

    def nextTurn(self):
        GameObject.nextTurn(self)

    def toList(self):
        list = GameObject.toList(self)
        list.extend([self.x, self.y, self.z])
        return list

    def addToMap(self):
        self.game.world.periods[self.z].area[(self.x, self.y)].append(self)

    def removeFromMap(self):
        self.game.world.periods[self.z].area[(self.x, self.y)].remove(self)
