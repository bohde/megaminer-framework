import game.base as base
import unittest
import collections

def string_exception(e):
    return ', '.join(str(n) for n in [e.__class__, e])

class TestBaseObjects(unittest.TestCase):

    def setUp(self):
        self.world = base.RectangularGameWorld(10, 10)

    def test_build_world(self):
        self.assertFalse(self.world == None)
        for k in (self.world.far_past, self.world.past, self.world.present):
            self.assertFalse(k == None)
            self.assertFalse(k.area == None)

    def test_lookup(self):
        for k in (self.world.far_past, self.world.past, self.world.present):
            self.assertTrue(isinstance(k.area, collections.defaultdict))
            try:
                k.area[1]
            except Exception, e:
                self.assertTrue(isinstance(e, TypeError), string_exception(e))
            try:
                k.area[(1,2,3)]
            except Exception, e:
                self.assertTrue(isinstance(e, TypeError), string_exception(e))
            try:
                k.area[('a',1)]
            except Exception, e:
                self.assertTrue(isinstance(e, TypeError), string_exception(e))
            try:
                k.area[(11,10)]
            except Exception, e:
                self.assertTrue(isinstance(e, IndexError), string_exception(e))
            e = 10
            try:
                k.area[(0,0)].append(e)
                self.assertTrue(e in k.area[(0,0)])
            except Exception, e:
                self.fail()

