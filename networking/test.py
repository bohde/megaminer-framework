#!/usr/bin/env python
from dispatch import DispatchProtocol
from apps import BaseApp, protocolmethod, namedmethod
from itertools import repeat


import time

def fact(n):
    return reduce(lambda x,y: x*y, xrange(1,n))

class Ping(BaseApp):
    @protocolmethod
    def ping(self):
        """ returns "pong" """
        return "pong"

    @protocolmethod
    def fat_ping(self):
        """ returns "pong" a whole bunch"""
        return [["pong"] for x in xrange(10000)]

    @protocolmethod
    def null(self):
        """ returns whatever is in self.value """
        return self.value

    @namedmethod("burn")
    def burn(self):
        """ sets self.value to 5! """
        self.value = fact(5)
        return None

    @protocolmethod
    def fat_burn(self):
        """ computes 1000! """
        fact(1000)
        return None

    @protocolmethod
    def whoami(self):
        return self.protocol.session_num

class TestLatencyServer(DispatchProtocol):
    apps = {
        "ping":Ping,
        }

if __name__ == "__main__":
    TestLatencyServer.print_protocol()
    TestLatencyServer.main()
