import itertools
import collections
import functools

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
        if abs(x) > self.max_x or abs(y) > self.max_y:
            raise IndexError('(%u, %u) is not within (-+%u, -+%u)' % (x, y, self.max_x, self.max_y))
        return collections.defaultdict.__missing__(self, key)


class TimePeriod(object):
    def __init__(self, factory):
        self.area = factory()


def basicMapGeneration(far_past, past, present):
    """
    Does nothing right now, but useful for testing.
    Use this as a template for more advanced map generation
    """
    return far_past, past, present


def rectangularAreasBuilder(x, y, f):
    """
    builds a rectange from (-x,-y) to (x,y)
    f is a function to populate the map
    """
    def generator():
        fact = lambda: RectangularArea(x, y)
        far_past, past, present = (TimePeriod(fact) for n in xrange(3))
        return f(far_past, past, present)
    return generator

class GameWorld(object):
    """
    Base class for a game world object
    """
    def __init__(self, generator):
        self.far_past, self.past, self.present = generator()
        self.periods = [self.far_past, self.past, self.present]


class RectangularGameWorld(GameWorld):
    """
    A rectangular game world object. This will probably be used, but I didn't want to restrict us.
    Shorthand for GameWorld(rectangularAreasBuilder(x,y, basicMapGeneration)) . 
    """
    def __init__(self, x, y):
        rectangularAreas = functools.partial(rectangularAreasBuilder, f=basicMapGeneration)
        GameWorld.__init__(self, rectangularAreas(x, y))

DefaultGameWorld = RectangularGameWorld
