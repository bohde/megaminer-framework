"""

   Copyright (C) 2008 by Steven Wallace
   snwallace@gmail.com

    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the
    Free Software Foundation, Inc.,
    59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
 """
"""
    Stephen Mues : I am 90% sure this is just an old relic from previous
                   games.  I don't think it does anything.
"""

from Server import *
from Filter import *

class PrintFilter(Filter):
    def begin(self):
        self.writeOut("test!" * 4000)
    
    def readOut(self, data):
        print data

class DumpFilter(Filter):
    def readIn(self, data):
        print "Read In: ", data
        Filter.readIn(self, data)
    
    def readOut(self, data):
        print "Read Out: ", data
        Filter.readOut(self, data)

server = TCPServer(None, DumpFilter(), PacketizerFilter(), CompressionFilter(), PrintFilter())
server.openConnection('127.0.0.1', 2100)
server.run()
