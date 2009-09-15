#!/usr/bin/python

from filters.GameFilter import GameFilter
from statements.GameStatements import statements
from test import MockConnection
import sys

def game_filter():
	gf = GameFilter()
	gf.statements = statements
	return gf

class testClient(object):
	def __init__(self):
		self.connection = MockConnection([game_filter])
		self.connection.begin()
		
	def readConsole(self):
		try:
			while 1:
				message = raw_input()
				self.send(message)
		except KeyboardInterrupt, k:
			print ""
			sys.exit(0)
		except Exception, e:
			sys.exit(1)

	def send(self, message):
		 print self.connection.request(message)
		
    

if __name__ == "__main__":
	x = testClient()
	x.readConsole()
	pass
