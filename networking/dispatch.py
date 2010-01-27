#!/usr/bin/env python

from twisted.internet import epollreactor
epollreactor.install()

from sexpr.sexpr import sexpr2str, str2sexpr

from twisted.internet import protocol, reactor, defer
from twisted.protocols.basic import LineReceiver
from itertools import repeat

class DispatchProtocol(LineReceiver):
    apps = {}
    sessions = 0

    def connectionMade(self):
        self.session_num = DispatchProtocol.sessions
        DispatchProtocol.sessions += 1
        self.apps = {}
        for key,app in self.__class__.apps.iteritems():
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
                    r = app.run(x[1:])
                    yield r
            return list(execute())
        d.addCallback(dispatch_to_apps)

        def write(output):
            self.transport.write(sexpr2str(*output))
        d.addCallback(write)
