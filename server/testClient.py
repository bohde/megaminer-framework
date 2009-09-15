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
		connection = MockConnection([game_filter])
	def readConsole(self):
		try:
			while 1:
				message = raw_input()
				self.send(message)
		except:
			sys.exit(1)
	def send(self, message):
		 print connection.request(message)
		
    

if __name__ == "__main__":
	x = testClient()
	x.readConsole()
	pass
