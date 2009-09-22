#!/usr/bin/python
import unittest
import networking.Filter as Filter
import main
import threading
import functools
from filters.GameServer import GameServer, GameFilter

class LoginException(Exception):
    pass

class MockConnection(Filter.Filter):
    def __init__(self, filters):
        Filter.Filter.__init__(self)
        self.filters = [a() for a in filters]
        reduce(Filter.cascadeSetIn, [self] + self.filters)
        self.response = ""

    def write(self, s):
        self.response = ""
        self.filters[0].readOut(s)

    def _writeOut(self, data):
        self.response = data

    def request(self, r):
        self.write(r)
        return self.response

class TestProtocolLogic(unittest.TestCase):
    def setUp(self):
        self.conn = MockConnection([main.RedirectFilter])
        self.conn.begin()
        master = self.conn.filters[0]
        master.address ='127.0.0.1'
        master.ID = 0


    def login(self):
        if not(self.conn.request('(login slave 12345)') == '("login-accepted" 1.000000)'):
            raise LoginException("LOGIN FAILED!")

    def assertContains(self, cont, obj, msg=None):
        self.assertTrue(obj in cont, msg)

    def assertResponseClosure(f):
        def wrapper(self, request, response, msg=None):
            f(self, self.conn.request(request), response, msg)
        return wrapper

    assertResponseContains = assertResponseClosure(assertContains)
    assertResponseIs = assertResponseClosure(unittest.TestCase.assertEquals)

    def requireLogin(self, request, response, msg=None):
        try:
            self.assertResponseContains(request, 'not logged in')
            self.login()
            self.assertResponseIs(request, response, msg)
        except Exception, e:
            raise e

    def testPing(self):
        self.assertResponseIs('(ping)', '("pong")')

    def testWhoAmI(self):
        self.assertResponseIs('(whoami)', '("who-you-are" ("id" 0) ("address" "127.0.0.1"))')

    def testRegisterServer(self):
        self.requireLogin('(register-server)', '("registered-status" "successful")')
        self.assertResponseIs('(list-servers)', '("servers" ((0 "127.0.0.1")))')

    def testGetServer(self):
        self.testRegisterServer()
        self.assertResponseIs('(get-server)', '("server" 0 "127.0.0.1")')

    def testStartGame(self):
        self.assertResponseContains('(start-game)', 'not logged in')
        self.testRegisterServer()
        self.assertResponseIs('(start-game)', '("game-number" 0 ("server" 0 "127.0.0.1"))')
        self.assertResponseIs('(join-game 0)', '("server" 0 "127.0.0.1")')
        self.assertResponseIs('(end-game 0)', '("game-ended" 0)')
        self.assertResponseIs('(join-game 0)', '("join-game-denied" ("invalid-number" "0"))')
        self.assertResponseIs('(end-game 0)', '("end-game-denied" ("invalid-number" "0"))')
    

class TestGameServer(unittest.TestCase):
    def setUp(self):
        self.server = GameServer('localhost', '19001')

    def testFilterIsSubclassOfGameFilter(self):
        self.assertTrue(isinstance(self.server.GameFilter(), GameFilter))

    def testInjection(self):
        def message(self):
            self.message = "Injected message before the function, called with arg " + str(self)
        GameServer.CustomGameFilter.__init__ = GameServer.CustomGameFilter.runFunctionAfterMethod(message)(GameServer.CustomGameFilter.__init__)
        try:
            self.server.message
            self.fail()
        except AttributeError:
            pass
        self.server.GameFilter()
        self.assertTrue("Injected message before the function, called with arg " + str(self.server)  in self.server.message)
    

if __name__ == '__main__':
    unittest.main()
