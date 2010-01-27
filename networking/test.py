#!/usr/bin/env python
from dispatch import DispatchProtocol
from apps import BaseApp
from itertools import repeat
from twisted.internet import protocol, reactor

import time

def fact(n):
    return reduce(lambda x,y: x*y, xrange(1,n))

class Ping(BaseApp):
    def ping(self, *args):
        return "pong"

    def fat_ping(self, *args):
        return [["pong"] for x in xrange(10000)]

    def null(self, *args):
        return self.value

    def burn(self, *args):
        self.value = fact(5)
        return None

    def fat_burn(self, *args):
        fact(1000)
        return [["phat"] for x in xrange(10)]

    def whoami(self, *args):
        return self.protocol.session_num

    mapper = {"ping":ping,
              "fat-ping":fat_ping,
              "null": null,
              "burn":burn,
              "fat-burn":fat_burn,
              "whoami":whoami,
              }

class TestLatencyServer(DispatchProtocol):
    apps = {
        "ping":Ping,
        }

if __name__ == "__main__":
    f = protocol.ServerFactory()
    f.protocol = TestLatencyServer
    reactor.listenTCP(3001, f)
    reactor.run()
