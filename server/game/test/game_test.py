import server.game.base as base
import unittest
import collections


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
            except Exception as e:
                self.assertTrue(isinstance(e, TypeError))
            try:
                k.area[(1,2,3)]
            except Exception as e:
                self.assertTrue(isinstance(e, TypeError))
            try:
                k.area[('a',1)]
            except Exception as e:
                self.assertTrue(isinstance(e, TypeError))
            try:
                k.area[(11,10)]
            except Exception as e:
                self.assertTrue(isinstance(e, IndexError))
            e = 10
            try:
                k.area[(0,0)].append(e)
                self.assertTrue(e in k.area[(0,0)])
            except Exception as e:
                self.fail()

