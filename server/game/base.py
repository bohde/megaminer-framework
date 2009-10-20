import itertools
import collections
import functools
import random
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


def initialSetup(game):
    """
    Places the initial buildings and units for the players
    """

    schoolType = game.getType("School")
    engineerType = game.getType("Engineer")
    galleryType = game.getType("Gallery")
    artistType = game.getType("Artist")
    farmType = game.getType("Farm")

    h = schoolType.height + galleryType.height + farmType.height
    w = max([schoolType.width, galleryType.width, farmType.width])
    x = 0
    y = 0

    while (x + y < game.periods[1].area.max_x / 2):
        x = random.randint(0, game.periods[1].area.max_x - w)
        y = random.randint(0, game.periods[1].area.max_y - h)

    #Buildings for player 0
    game.addObject(Building(game, x, y, 0, game.players[0], schoolType, 0))
    game.addObject(Building(game, x, y + schoolType.height, 0, game.players[0], galleryType, 0))
    game.addObject(Building(game, x, y + schoolType.height + galleryType.height,
                            0, game.players[0], farmType, 0))

    # Units for player 0
    for z in xrange(3):
        game.addObject(Unit(game, x, y, z, game.players[0], engineerType, 0))
        game.addObject(Unit(game, x, y + schoolType.height, z, game.players[0], artistType, 0))

    x = -x - w + 1
    y = -y - h + 1

    # Buildings for player 1
    game.addObject(Building(game, x, y, 0, game.players[0], farmType, 0))
    game.addObject(Building(game, x, y + farmType.height, 0, game.players[0], galleryType, 0))
    game.addObject(Building(game, x, y + farmType.height + galleryType.height,
                            0, game.players[0], schoolType, 0))

    # Units for player 1
    for z in xrange(3):
        game.addObject(Unit(game, x, y + farmType.height + galleryType.height,
                       z, game.players[1], engineerType, 0))
        game.addObject(Unit(game, x, y + schoolType.height, z, game.players[1], artistType, 0))


def portalDisCheck(game, farPastPortals, x, y):
    """
    Returns False if the distance between the supplied point and any portal
    in the supplied list is less than a minimum
    """

    MIN_DIS = 3 # To config file?
    for p in farPastPortals:
        if game.distance(x, y, p.x, p.y) < MIN_DIS:
            return False
    return True


def basicMapGeneration(game):
    """
    Adds initial buildings and units and generates terrain and portals
    """

    initialSetup(game)

    n = 10 # To config file?
    t = 10 # To config file?
    numPortals = 0
    numTerrain = 0
    farPastPortals = []

    # Pick portals linking far past and past
    while (numPortals <= n):
        x = random.randint(-game.periods[1].area.max_x, game.periods[1].area.max_x)
        y = random.randint(-game.periods[1].area.max_y, game.periods[1].area.max_y)
        if game.periods[1].area[(x, y)] == [] and (game.periods[1].area[(-x, -y)] == []):
            farPastPortals.append(Portal(game, x, y, 1, -1))
            game.addObject(farPastPortals[-1])
            farPastPortals.append(Portal(game, -x, -y, 1, -1))
            game.addObject(farPastPortals[-1])
            game.addObject(Portal(game, x, y, 0, 1))
            game.addObject(Portal(game, -x, -y, 0, 1))
            numPortals += 2

    # Pick portals linking past and present
    numPortals = 0
    while (numPortals <= n):
        x = random.randint(-game.periods[1].area.max_x, game.periods[1].area.max_x)
        y = random.randint(-game.periods[1].area.max_y, game.periods[1].area.max_y)
        if game.periods[1].area[(x, y)] == [] \
                and (game.periods[1].area[(-x, -y)] ==  []) \
                and portalDisCheck(game, farPastPortals, x, y):
            game.addObject(Portal(game, x, y, 1, 1))
            game.addObject(Portal(game, -x, -y, 1, 1))
            game.addObject(Portal(game, x, y, 2, -1))
            game.addObject(Portal(game, -x, -y, 2, -1))
            numPortals += 2

            game.addObject(Terrain(game, x, y, 0, True, True))
            game.addObject(Terrain(game, -x, -y, 0, True, True))

    # Add blocking terrain
    for z in xrange(3):
        numTerrain = 0
        while (numTerrain <= t):
            x = random.randint(-game.periods[z].area.max_x, game.periods[z].area.max_x)
            y = random.randint(-game.periods[z].area.max_y, game.periods[z].area.max_y)
            if (game.periods[z].area[(x, y)] == []) and (game.periods[z].area[(-x, -y)] == []):
                game.addObject(Terrain(game, x, y, z, True, True))
                game.addObject(Terrain(game, -x, -y, z, True, True))
                numTerrain += 2


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
