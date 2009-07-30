import unittest
import game.test
import networking.Filter as Filter
import main
import threading
from game.test import *
import functools

class LoginException(Exception):
    pass


class MockConnection(Filter.Filter):
    def __init__(self, filters):
        self.filters = [a() for a in filters]
        reduce(Filter.cascadeSetIn, [self] + self.filters)
        self.done = threading.Event()
        self.response = ""
        Filter.Filter.__init__(self)

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

    def assertResponseIs(self, request, response, text=None):
        self.assertEquals(self.conn.request(request), response, text)

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


if __name__ == '__main__':
    unittest.main()
