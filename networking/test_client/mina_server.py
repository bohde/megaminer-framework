#!/usr/bin/env python

from twisted.internet import epollreactor
epollreactor.install()

from sexpr.sexpr import sexpr2str, str2sexpr

from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver
from itertools import repeat

import time

class BaseApp(object):
    def run(self, commands):
        pass

    def state(self):
        return []

class Ping(BaseApp):
    def state(self):
        return ["pong"]

class FatPing(BaseApp):
    def state(self):
        return list(repeat(["pong"], 10000))

class DispatchProtocol(LineReceiver):
    apps = {
        "ping":Ping,
        "fat-ping":FatPing,
        }

    sessions = 0

    def connectionMade(self):
        self.session_num = DispatchProtocol.sessions
        DispatchProtocol.sessions += 1
        
    def lineReceived(self, line):
        sxpr = str2sexpr(line)
        for x in str2sexpr(line):
            app = DispatchProtocol.apps[x[0]]
            running_app = app()
            running_app.run(x[1:])
            self.transport.write(sexpr2str(running_app.state()))
        
class TestLatencyServer(DispatchProtocol):
    t = time.time()

    def lineReceived(self, line):
        DispatchProtocol.lineReceived(self, line)
        t = time.time()
        print t - TestLatencyServer.t
        TestLatencyServer.t = t

if __name__ == "__main__":
    f = protocol.ServerFactory()
    f.protocol = TestLatencyServer
    reactor.listenTCP(3001, f)
    reactor.run()
