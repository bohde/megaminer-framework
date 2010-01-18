#!/usr/bin/env python

from twisted.internet import epollreactor
epollreactor.install()

from twisted.internet import protocol, reactor, defer
import random

#import psyco
#psyco.full()

clients = []
class TestClient(protocol.Protocol):
    
    i = 0
    def connectionMade(self):
        self.n = TestClient.i
        TestClient.i += 1

    def send_message(self):
        self.transport.write('("fat-ping" %d)\r\n'%(self.n))
        
def protocol_created(p):
    clients.append(p)

def pick_and_send():
    if clients: random.choice(clients).send_message()
    reactor.callLater(0.05, pick_and_send)

def start_sessions():
    for i in range(1000):
        cc = protocol.ClientCreator(reactor, TestClient)
        d = cc.connectTCP("127.0.0.1", 3001)
        d.addCallback(protocol_created)
    reactor.callLater(0, pick_and_send)

reactor.callLater(0, start_sessions)
reactor.run()
