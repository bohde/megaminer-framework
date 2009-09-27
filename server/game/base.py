import itertools
import collections
import functools
from portal import *
from terrain import *
from unit import *
from building import *

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
    Adds some basic objects to the map.
    """
    schoolType = game.getType("School")
    engineerType = game.getType("Engineer")
    galleryType = game.getType("Gallery")
    artistType = game.getType("Artist")
    farmType = game.getType("Farm")

    #Buildings
    game.addObject(Building(game, -10, -10, 0, game.players[0], schoolType, 0))
    game.addObject(Building(game, -10, -8, 0, game.players[0], galleryType, 0))
    game.addObject(Building(game, -8, -10, 0, game.players[0], farmType, 0))

    game.addObject(Building(game, 9, 9, 0, game.players[1], schoolType, 0))
    game.addObject(Building(game, 7, 9, 0, game.players[1], galleryType, 0))
    game.addObject(Building(game, 9, 7, 0, game.players[1], farmType, 0))

    #Units
    for z in xrange(3):
        game.addObject(Unit(game, -10,-10,z, game.players[0], engineerType, 0))
        game.addObject(Unit(game, -10, -8, z, game.players[0], artistType, 0))
        game.addObject(Unit(game, 9, 9, z, game.players[1], engineerType, 0))
        game.addObject(Unit(game, 7, 9, z, game.players[1], artistType, 0))

    #Portals
    #  Far past and Past
    game.addObject(Portal(game, 10, 0, 0, 1))
    game.addObject(Portal(game, 10, 0, 1, -1))
    game.addObject(Portal(game, -10, 0, 0, 1))
    game.addObject(Portal(game, -10, 0, 1, -1))

    #  Past and Present
    game.addObject(Portal(game, 0, 10, 1, 1))
    game.addObject(Portal(game, 0, 10, 2, -1))
    game.addObject(Portal(game, 0, -10, 1, 1))
    game.addObject(Portal(game, 0, -10, 2, -1))

    newTerrain = []
    for z in range(3):
        newTerrain.append(Terrain(game, 0, 0, z))
        newTerrain[z].blockMove = True
        newTerrain[z].blockBuild = True
        game.addObject(newTerrain[z])

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
