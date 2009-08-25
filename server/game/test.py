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
        """
        Tests Match.addPlayer and Match.nextTurn
        """
        self.assertEqual(self.game.players, [])
        self.game.addPlayer(self.players[0])
        self.assertNotEqual(True, self.game.start())
        self.assertEqual([self.players[0]], self.game.players)
        self.game.addPlayer(self.players[1])
        self.assertEqual(self.players, self.game.players)
        self.assertNotEqual(True, self.game.addPlayer(MockPlayer()))
        self.assertEqual(True, self.game.start())
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

    def test_load_units(self):
        """
        Tests Match.loadUnitSet and Match.addObject applied to units and
        unit types.
        """
        self.game.loadUnitSet("config/testUnitSet.cfg")
        wolfType = self.game.objects.get(self.game.nextid - 2)
        pandaType = self.game.objects.get(self.game.nextid - 1)
        self.assertEqual(pandaType.name, "Panda")
        self.assertTrue(pandaType.cute and not pandaType.deadly)
        self.assertEqual(wolfType.name, "Wolf")
        self.assertTrue(not wolfType.cute and wolfType.deadly)
        previd = self.game.nextid
        self.unit = Unit(self.game, 3, 7, 0, self.players[0], pandaType)
        self.assertEqual(previd + 1, self.game.nextid)
        self.game.addObject(self.unit)
        self.assertEqual(self.game.objects.get(self.unit.id), self.unit)
        self.assertEqual(self.game.world.periods[0].area[(3,7)], [self.unit])

    def test_load_buildings(self):
        """
        Tests Match.loadBuildingSet and Match.addObject applied to buildings
        """
        previd = self.game.nextid
        self.game.loadBuildingSet("config/testBuildingSet.cfg")
        self.assertEqual(previd + 1, self.game.nextid)
        houseType = self.game.objects.get(self.game.nextid - 1)
        self.assertEqual(houseType.name, "House")
        self.assertTrue(houseType.fancy)
        self.home = Building(self.game, 4, 7, 0, self.players[0], houseType)
        self.game.addObject(self.home)
        self.assertEqual(self.game.objects.get(self.home.id), self.home)
        self.assertEqual(self.game.world.periods[0].area[(4,7)], [self.home])
        self.assertEqual(self.home.hp, 44)


class TestActions(unittest.TestCase):
    def setUp(self):
        self.game = Match(1)
        self.players = [MockPlayer(), MockPlayer()]
        self.game.addPlayer(self.players[0])
        self.game.addPlayer(self.players[1])
        self.game.loadUnitSet("config/testUnitSet.cfg")
        self.wolfType = self.game.objects.get(self.game.nextid - 2)
        self.pandaType = self.game.objects.get(self.game.nextid - 1)
        self.units = []
        self.units.append(Unit(self.game,3,7,0,self.players[0],self.wolfType))
        self.units.append(Unit(self.game,3,6,0,self.players[1],self.pandaType))
        self.game.addObject(self.units[0])
        self.game.addObject(self.units[1])
        self.game.loadBuildingSet("config/testBuildingSet.cfg")
        self.houseType = self.game.objects.get(self.game.nextid - 1)
        self.home = Building(self.game, 4,7,0, self.players[0],self.houseType)
        self.game.addObject(self.home)
        self.game.start()
    
    def test_attack(self):
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.game.nextTurn()
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.game.nextTurn()
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 4, 9))
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 7))
        self.assertEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.assertEqual(self.game.objects.get(self.units[1].id).hp, 41)
        self.assertEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.assertEqual(None, self.game.objects.get(self.units[1].id))
        self.assertEqual([], self.game.world.periods[0].area[(3,6)])
        self.assertNotEqual(True, self.game.attack(234, 3, 6))
        self.assertNotEqual(True, self.game.attack(self.units[1].id, 3, 7))

    def test_move(self):
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.game.nextTurn()
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.game.nextTurn()
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 9))
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 10))
        self.game.nextTurn()
        self.game.nextTurn()
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 10))
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 11))

    def test_build(self):
        x, y = 4, 6
        builderID = int(self.units[1].id)
        typeID = int(self.houseType.id)
        attemptBuild = lambda: self.game.build(builderID, x, y, typeID)
        self.assertNotEqual(True, attemptBuild())
        self.game.nextTurn()
        y = 9
        self.assertNotEqual(True, attemptBuild())
        y = 6
        self.assertEqual(True, attemptBuild())
        newHouse = self.game.world.periods[0].area[(x,y)][0]
        self.assertEqual(newHouse.type.name, "House")
        self.assertNotEqual(True, attemptBuild())
        self.game.nextTurn()
        builderID = int(self.units[0].id)
        self.assertNotEqual(True, attemptBuild())
