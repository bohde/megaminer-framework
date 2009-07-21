import json
import itertools
import collections

def lookupFactory(max_x, max_y):
    """
    if something isn't there return a new list
    if out of bounds, return IndexError
    """
    def lookup(coord):
        if not(isinstance(coord, collections.Sequence)):
            raise TypeError('%s is not a subclass of Sequence.' % n.__class__)
        if len(coord) != 2:
            raise TypeError('A coordinate does not have a length of %n!' % len(coord))
        x, y = coord
        if abs(x) > max_x or abs(y) > max_y:
            raise IndexError('(%n, %n) is not within (-+%n, -+%n)' % (x, y, max_x, max_y))
        return []
    return lookup


def standard(x, y):
    def generator():
        fact = lookupFactory(x, y)
        far_past, past, present = (TimePeriod(fact) for x in xrange(3))

        """
        put map building logic here
        """

        return far_past, past, present
    return generator


class TimePeriod(object):
    def __init__(self, factory):
        area = collections.defaultdict(factory)


class GameWorld(object):
    def __init__(self, generator):
        self.far_past, self.past, self.present = generator()