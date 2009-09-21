import itertools
import collections
import functools
from portal import *
from terrain import *

class RectangularArea(collections.defaultdict):
    """
    The actual "board". Lookup on either a tuple or list of two integers. Can be thought of a matrix from (-x,-y) to (x,y).
    Returns a list of the objects at that location.
    """
    def __init__(self, max_x, max_y):
        collections.defaultdict.__init__(self, list)
        self.max_x = max_x
        self.max_y = max_y

    def __missing__(self, key):
        if not(isinstance(key, (list, tuple))):
                raise TypeError('%s is not a list or tuple.' % key.__class__)
        if len(key) != 2:
            raise TypeError('A coordinate does not have a length of %u!' % len(key))
        if not(all([isinstance(n, int) for n in key])):
            raise TypeError('Coordinates need to be integers!')
        x, y = key
        if not self.inBounds(x,y):
            raise IndexError('(%u, %u) is not within (-+%u, -+%u)' % (x, y, self.max_x, self.max_y))
        return collections.defaultdict.__missing__(self, key)

    def inBounds(self, x, y):
        return (abs(x) <= self.max_x and abs(y) <= self.max_y)

class TimePeriod(object):
    def __init__(self, factory):
        self.area = factory()


def basicMapGeneration(game):
    """
    Does nothing right now, but useful for testing.
    Use this as a template for more advanced map generation
    """
    newPortal = Portal(game, 3, 2, 1, 1)
    game.addObject(newPortal)
    #assert(game.periods[1].area[(3,2)] == [newPortal])
    game.addObject(Terrain(game, 6, 3, 0))
    pass


def rectangularAreasBuilder(x, y):
    """
    builds a rectange from (-x,-y) to (x,y)
    f is a function to populate the map
    """
    def generator():
        fact = lambda: RectangularArea(x, y)
        far_past, past, present = (TimePeriod(fact) for n in xrange(3))
        return far_past, past, present
    return generator

class GameWorld(object):
    """
    Base class for a game world object
    """
    def __init__(self, generator):
        self.nextid = 0
        self.maxid = 2147483600
        self.turnNum = 0
        self.players = []
        self.turn = None #the player whose turn it is;
                         #None before and after the game.
        self.winner = None #the player who won the game;
                           #None before and during the game
        self.objects = dict() #key: object's id
                              #value: instance of the object
        self.animations = ["animations"]

        self.far_past, self.past, self.present = generator()
        self.periods = [self.far_past, self.past, self.present]

    def addObject(self, newObject):
        self.animations += [["add", newObject.id]]
        self.objects[newObject.id] = newObject
        if (isinstance(newObject, MappableObject)):
            newObject.addToMap()

    def removeObject(self, oldObject):
        self.animations += [["remove", oldObject.id]]
        if isinstance(oldObject, MappableObject):
            oldObject.removeFromMap()
        del self.objects[oldObject.id]


class RectangularGameWorld(GameWorld):
    """
    A rectangular game world object. This will probably be used, but I didn't want to restrict us.
    Shorthand for GameWorld(rectangularAreasBuilder(x,y, basicMapGeneration)) . 
    """
    def __init__(self, x, y):
        GameWorld.__init__(self, rectangularAreasBuilder(x, y))

    def distance(self, startX, startY, endX, endY):
        return abs(startX - endX) + abs(startY - endY)

DefaultGameWorld = RectangularGameWorld
