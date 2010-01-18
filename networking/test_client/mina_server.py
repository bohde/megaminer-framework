#!/usr/bin/env python

from twisted.internet import epollreactor
epollreactor.install()

from sexpr.sexpr import sexpr2str, str2sexpr

from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver
import time

class BaseApp(object):
    def run(self, commands):
        print self.__class__

    def state(self):
        return []

class Ping(BaseApp):
    def state(self):
        return ["pong"]

class FatPing(BaseApp):
    def state(self):
        return [["pong"] for x in xrange(1337)]

class DispatchProtocol(LineReceiver):
    apps = {
        "ping":Ping,
        "fat-ping":FatPing,
        }

    def lineReceived(self, line):
        sxpr = str2sexpr(line)
        for x in str2sexpr(line):
            app = DispatchProtocol.apps[x[0]]
            running_app = app()
            running_app.run(x[1:])
            self.transport.write(sexpr2str(running_app.state()))
        
class TestLatencyServer(DispatchProtocol):
    i = 0
    t = time.time()

    def connectionMade(self):
        self.n = TestLatencyServer.i
        print "Created session", self.n
        TestLatencyServer.i += 1

    def lineReceived(self, line):
        DispatchProtocol.lineReceived(self, line)
        t = time.time()
        print "Received", line, "on session", self.n,  t - TestLatencyServer.t
        TestLatencyServer.t = t

if __name__ == "__main__":
    f = protocol.ServerFactory()
    f.protocol = TestLatencyServer
    reactor.listenTCP(3001, f)
    reactor.run()
