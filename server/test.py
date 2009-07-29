import unittest
import game.test
import networking.Filter as Filter
import main
import threading
from game.test import *

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


class TestProtocolLogic(unittest.TestCase):
    def setUp(self):
        self.conn = MockConnection([main.MasterFilter])
        master = self.conn.filters[0]
        master.address ='127.0.0.1'
        master.ID = 0

    def assertRequestGeneratesResponse(self, request, response):
        self.conn.write(request)
        self.assertEquals(self.conn.response, response)

    def testPing(self):
        self.assertRequestGeneratesResponse('(ping)', '("pong")')

    def testWhoAmI(self):
        self.assertRequestGeneratesResponse('(whoami)', '("who-you-are" ("id" 0) ("address" "127.0.0.1"))')

if __name__ == '__main__':
    unittest.main()
    unittest.main(game.test)
