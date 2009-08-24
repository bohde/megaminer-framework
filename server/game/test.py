import game.base as base
import unittest
import collections
from match import *

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

class MockPlayer(object):
    """
    An object to receive messages as if it were a player.  This class will
    be used to test the game code without having to rely on all the
    networking code.
    """
    def __init__(self):
        self.messages = [] #A list of messages this player has received

    def writeSExpr(self, message):
        self.messages.append(message)

    def last(self):
        return self.messages[len(self.messages) - 1]


class TestMatchStart(unittest.TestCase):
    def setUp(self):
        self.game = Match(1)
        self.players = [MockPlayer(), MockPlayer()]

    def test_join_game(self):
        self.assertEqual(self.game.players, [])
        self.game.addPlayer(self.players[0])
        self.assertNotEqual(True, self.game.start())
        self.assertEqual([self.players[0]], self.game.players)
        self.game.addPlayer(self.players[1])
        self.assertEqual(self.players, self.game.players)
        self.assertNotEqual(True, self.game.addPlayer(MockPlayer()))

    def test_turn_order(self):
        self.game.addPlayer(self.players[0])
        self.game.addPlayer(self.players[1])
        self.assertTrue(self.game.start())
        self.assertEqual(self.game.turn, self.players[0])
        self.game.nextTurn()
        self.assertEqual(self.game.turn, self.players[1])
        self.game.nextTurn()
        self.assertEqual(self.game.turn, self.players[0])


class TestObjectCreation(unittest.TestCase):
    def setUp(self):
        self.game =  Match(1)
        self.players = [MockPlayer(), MockPlayer()]
        self.game.addPlayer(self.players[0])
        self.game.addPlayer(self.players[1])
        self.game.start()

    def test_add_unit(self):
        previd = self.game.nextid
        self.unitType = UnitType(self.game)
        self.unit = Unit(self.game, 3, 7, 0, self.players[0], self.unitType)
        self.assertEqual(previd + 2, self.game.nextid)
        self.game.addObject(self.unitType)
        self.game.addObject(self.unit)
        self.assertEqual(self.game.objects.get(self.unit.id), self.unit)
        self.assertEqual(self.game.objects.get(self.unitType.id), \
                          self.unitType)
        self.assertEqual(self.game.world.periods[0].area[(3,7)], [self.unit])

    def test_config_unit_set(self):
        self.game.loadUnitSet("config/testUnitSet.cfg")
        wolf = self.game.objects.get(self.game.nextid - 2)
        panda = self.game.objects.get(self.game.nextid - 1)
        self.assertEqual(panda.name, "Panda")
        self.assertTrue(panda.cute and not panda.deadly)
        self.assertEqual(wolf.name, "Wolf")
        self.assertTrue(not wolf.cute and wolf.deadly)

class TestUnits(unittest.TestCase):
    def setUp(self):
        self.game = Match(1)
        self.players = [MockPlayer(), MockPlayer()]
        self.unitType = UnitType(self.game)
        self.units = []
        self.units.append(Unit(self.game,3,7,0,self.players[0],self.unitType))
        self.units.append(Unit(self.game,3,6,0,self.players[1],self.unitType))
        self.game.addObject(self.unitType)
        self.game.addObject(self.units[0])
        self.game.addObject(self.units[1])
        self.game.start()
    
    def test_attack(self):
        self.assertTrue(self.game.attack(self.units[0].id, 3, 6))
        try:
            self.assertFalse(self.game.attack(234, 3, 6))
            self.fail()
        except Exception, e:
            self.assertTrue(isinstance(e, KeyError), string_exception(e))
            
