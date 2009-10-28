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
        self.user = "Username"

    def writeSExpr(self, message):
        self.messages.append(message)

    def last(self):
        return self.messages[len(self.messages) - 1]


class TestMatchStart(unittest.TestCase):
    def setUp(self):
        self.game = Match(7000)
        self.players = [MockPlayer(), MockPlayer()]
        self.game.declareWinner = lambda self: None

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
        self.game =  Match(7001)
        self.game.declareWinner = lambda self: None
        self.players = [MockPlayer(), MockPlayer()]
        self.game.addPlayer(self.players[0])
        self.game.addPlayer(self.players[1])
        self.game.start()
        for key in xrange(self.game.nextid):
            if self.game.objects.has_key(key):
                self.game.removeObject(self.game.objects[key])

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
        self.unit = Unit(self.game, 3, 7, 0, self.players[0], pandaType, 0)
        self.assertEqual(previd + 1, self.game.nextid)
        self.game.addObject(self.unit)
        self.assertEqual(self.game.objects.get(self.unit.id), self.unit)
        self.assertEqual(self.game.periods[0].area[(3,7)], [self.unit])

    def test_load_buildings(self):
        """
        Tests Match.loadBuildingSet, Match.addObject applied to buildings,
           and Building.bringToCompletion
        """
        previd = self.game.nextid
        self.game.loadBuildingSet("config/testBuildingSet.cfg")
        self.assertEqual(previd + 2, self.game.nextid)
        houseType = self.game.getType("House")
        self.assertEqual(houseType.name, "House")
        self.assertTrue(houseType.fancy)
        self.home = Building(self.game, 4, 7, 0, self.players[0], houseType, 0)
        self.game.addObject(self.home)
        self.assertEqual(self.home.hp, 44)
        self.assertEqual(self.game.objects.get(self.home.id), self.home)
        self.assertEqual(self.game.periods[0].area[(4,7)], [self.home])
        self.assertEqual([], self.game.periods[1].area[(4,7)])
        self.home.bringToCompletion()
        pastHouse = self.game.periods[1].area[(4,7)][0]
        self.assertNotEqual([], self.game.periods[2].area[(4,7)])
        self.assertNotEqual([], self.game.periods[2].area[(5,7)])
        self.game.removeObject(pastHouse)
        self.assertEqual([], self.game.periods[2].area[(4,7)])


class TestActions(unittest.TestCase):
    def setUp(self):
        self.game = Match(7002)
        self.players = [MockPlayer(), MockPlayer()]
        self.game.addPlayer(self.players[0])
        self.game.addPlayer(self.players[1])
        self.game.loadUnitSet("config/testUnitSet.cfg")
        self.wolfType = self.game.getType("Wolf")
        self.pandaType = self.game.getType("Panda")
        self.units = []
        self.units.append(Unit(self.game, 3, 7, 0, self.players[0],
                                self.wolfType, 0))
        self.units.append(Unit(self.game, 3, 6, 0, self.players[1],
                                self.pandaType, 0))
        self.game.addObject(self.units[0])
        self.game.addObject(self.units[1])
        self.game.loadBuildingSet("config/testBuildingSet.cfg")
        self.houseType = self.game.getType("House")
        self.home = Building(self.game, 4, 7, 0, self.players[0],
                             self.houseType, 0)
        self.herbertType = self.game.getType("Herbert")
        self.herbert = Building(self.game, -5, 5, 2, self.players[1],
                             self.herbertType, 0)
        self.game.addObject(self.home)
        self.game.addObject(self.herbert)
        lastValidID = self.game.nextid - 1
        self.game.start()
        #Remove objects created upon map generation
        for key in xrange(self.game.nextid):
            if self.game.objects.has_key(key) and key > lastValidID:
                self.game.removeObject(self.game.objects[key])
    
    def test_attack(self):
        #No actions
        self.units[0].actions = 0
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.game.nextTurn()
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.game.nextTurn()
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 4, 9))
        self.assertNotEqual(True, self.game.attack(self.units[0].id, 3, 7))
        self.assertEqual(2, self.units[0].moves)        
        self.assertEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.assertEqual(1, self.units[0].moves)
        self.assertEqual(self.game.objects.get(self.units[1].id).hp, 41)
        self.assertEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.assertEqual(None, self.game.objects.get(self.units[1].id))
        self.assertEqual([], self.game.periods[0].area[(3,6)])
        self.assertNotEqual(True, self.game.attack(234, 3, 6))
        self.assertNotEqual(True, self.game.attack(self.units[1].id, 3, 7))
        self.game.nextTurn()

    def test_shelter(self):
        self.game.nextTurn()
        self.game.nextTurn()
        self.shelter = Building(self.game, 2, 6, 0, self.players[0],
                             self.houseType, 0)
        self.game.addObject(self.shelter)
        self.shelter.bringToCompletion()
        self.assertEqual(True, self.game.attack(self.units[0].id, 3, 6))
        self.assertTrue(self.shelter.hp < self.houseType.effHP(0))
        self.assertEqual(self.units[1].hp, self.pandaType.effHP(0))

    def test_move(self):
        #No moves
        self.units[0].moves = 0
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.game.nextTurn()
        #Not your unit
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.game.nextTurn()
        #Can not move onto enemy
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 6))
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 8))
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 9))
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 10))
        self.game.nextTurn()
        self.game.nextTurn()
        self.assertEqual(True, self.game.move(self.units[0].id, 3, 10))
        self.assertNotEqual(True, self.game.move(self.units[0].id, 3, 11))

    def test_build_cancel(self):
        """
        Tests both Unit.build and Building.cancel
        """
        x, y = 4, 6
        builderID = int(self.units[1].id)
        typeID = int(self.houseType.id)
        self.players[1].gold[0] = 180
        attemptBuild = lambda: self.game.build(builderID, x, y, typeID)
        self.assertNotEqual(True, attemptBuild()) #not your unit
        self.game.nextTurn()
        y = 9
        self.assertNotEqual(True, attemptBuild()) #not adjacent
        y = 6
        self.players[1].gold[0] = 0
        self.assertNotEqual(True, attemptBuild()) #no gold
        self.players[1].gold[0] = 180
        self.assertEqual(True, attemptBuild())
        self.assertEqual(29, self.players[1].gold[0])
        newHouse = self.game.periods[0].area[(x,y)][0]
        self.assertEqual(newHouse.type.name, "House")
        self.assertEqual(True, self.game.cancel(newHouse.id))
        self.assertEqual(180, self.players[1].gold[0])
        self.assertNotEqual(True, self.game.cancel(self.home.id)) #completed
        self.game.nextTurn()
        builderID = int(self.units[0].id)
        x = 3
        self.assertNotEqual(True, attemptBuild())

    def test_train(self):
        """
        tests both Building.train and Building.cancel
        """
        self.game.nextTurn()
        builderID = self.home.id
        newUnitTypeID = self.pandaType.id
        attemptTrain =lambda: self.game.train(builderID, newUnitTypeID)
        self.players[0].gold[0] = 106
        self.assertNotEqual(True, attemptTrain()) #Not your turn
        builderID = self.units[1].id
        self.assertNotEqual(True, attemptTrain()) #Not a building
        builderID = self.home.id
        self.game.nextTurn()
        self.players[0].gold[0] = 0
        self.assertNotEqual(True, attemptTrain()) #No money
        self.players[0].gold[0] = 106
        newUnitTypeID = self.wolfType.id
        self.assertNotEqual(True, attemptTrain()) #Invalid unit type
        newUnitTypeID = self.pandaType.id
        self.assertEqual(True, attemptTrain())
        self.assertEqual(3, self.players[0].gold[0])
        #cancel
        self.assertEqual(True, self.game.cancel(self.home.id))
        self.assertEqual(106, self.players[0].gold[0])
        #restart
        self.assertEqual(True, attemptTrain())
        self.assertEqual(3, self.players[0].gold[0])
        #wait for completion

        for i in range(0, self.pandaType.trainTime * 2 - 1):
            self.game.nextTurn()
        previd = int(self.game.nextid)
        self.game.nextTurn()
        self.assertEqual(previd + 1, self.game.nextid)
        self.assertEqual(5, self.game.objects[previd].x)

    def test_hunger(self):
        self.game.declareWinner = lambda self: None
        self.game.nextTurn()
        self.assertEqual(21, self.units[0].hp)
        self.game.removeObject(self.home)
        self.game.nextTurn()
        self.assertEqual(16, self.units[0].hp)
        self.game.nextTurn()
        self.assertEqual(16, self.units[0].hp)

    def test_paint(self):
        attemptPaint = lambda: self.game.paint(self.units[0].id, 4, 7)
        self.units[0].actions = 0
        self.assertNotEqual(True, attemptPaint()) #No actions
        self.game.nextTurn()
        self.assertNotEqual(True, attemptPaint()) #Not your unit
        self.game.nextTurn()
        self.assertEqual(True, attemptPaint())

    def test_warp(self):
        portal = Portal(self.game,3,6,0,1)
        self.game.addObject(portal)
        self.game.nextTurn()
        self.players[1].gold[0] = portal.fee
        self.game.warp(self.units[1].id)
        self.assertEqual(1, self.units[1].z)
        self.assertEqual(0, self.players[1].gold[0])

    def test_win_annihilation(self):
       for t in xrange(20):
           self.game.nextTurn()
       self.assertEqual(self.game.winner, None)
       self.game.removeObject(self.herbert)
       self.game.nextTurn()
       self.assertEqual(self.game.winner, self.players[0])

    def test_win_turn_limit(self):
        for t in xrange(self.game.turnLimit-1):
            self.game.nextTurn()
        self.assertEqual(self.game.winner, None)
        self.game.nextTurn()
        self.assertEqual(self.game.winner, self.players[1])


