from gameObject import *

class MappableObject(GameObject):
    """
    All objects that are associated with a single x, y location will
    inherit from this class.
    """

    def __init__(self, game, x, y):
        GameObject.__init__(self, game)
        self.x = x
        self.y = y

    def nextTurn(self):
        GameObject.nextTurn(self)

    def toList(self):
        list = GameObject.toList(self)
        list.extend([self.x, self.y])
        return list

