import json
import itertools
import collections
import functools

class RectangularArea(collections.defaultdict):
    def __init__(self, max_x, max_y):
        collections.defaultdict.__init__(self, list)
        self.max_x = max_x
        self.max_y = max_y

    def __missing__(self, key):
        if not(isinstance(key, collections.Sequence)):
                raise TypeError('%s is not a subclass of Sequence.' % key.__class__)
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
    return far_past, past, present


def rectangularAreasBuilder(x, y, f):
    def generator():
        fact = lambda: RectangularArea(x, y)
        far_past, past, present = (TimePeriod(fact) for n in xrange(3))
        return f(far_past, past, present)
    return generator


rectangularAreas = functools.partial(rectangularAreasBuilder, f=basicMapGeneration)


class GameWorld(object):
    def __init__(self, generator):
        self.far_past, self.past, self.present = generator()


class RectangularGameWorld(GameWorld):
    def __init__(self, x, y):
        GameWorld.__init__(self, rectangularAreas(x, y))