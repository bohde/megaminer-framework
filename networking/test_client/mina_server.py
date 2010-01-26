#!/usr/bin/env python

from twisted.internet import epollreactor
epollreactor.install()

from sexpr.sexpr import sexpr2str, str2sexpr

from twisted.internet import protocol, reactor, defer

from twisted.protocols.basic import LineReceiver
from itertools import repeat

import time

class BaseApp(object):
    def __init__(self, protocol):
        self.protocol = protocol
    
    def run(self, commands):
        def apply(coms):
            return self.__class__.mapper[coms[0]](self, coms[1:])
        return filter(bool, map(apply, commands))
                        
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

class DispatchProtocol(LineReceiver):
    apps = {
        "ping":Ping,
        }
    sessions = 0

    def connectionMade(self):
        self.session_num = DispatchProtocol.sessions
        DispatchProtocol.sessions += 1
        self.apps = {}
        for key,app in DispatchProtocol.apps.iteritems():
            self.apps[key] = app(self)
        
    def lineReceived(self, line):
        d = defer.succeed(line)

        def onError(err):
            return "Internal server error"
        d.addErrback(onError)

        def convert_to_lists(line):
            return str2sexpr(line)
        d.addCallback(convert_to_lists)

        def dispatch_to_apps(commands):
            def execute():
                for x in commands:
                    app = self.apps[x[0]]
                    yield app.run(x[1:])
            return list(execute())
        d.addCallback(dispatch_to_apps)

        def write(output):
            self.transport.write(sexpr2str(*output))
        d.addCallback(write)
            
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
