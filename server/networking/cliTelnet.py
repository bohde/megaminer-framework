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
    File : cliTelnet.py

    Arguments : python cliTelnet.py ipAddress portNumber
                python cliTelnet.py
                   - defaults to localhost, port 19000

    Purpose : This file is used for preliminary testing of the server, 
              mostly for whoever is programming the game rules (Game.py).
              This is a handy little file because it allows you to send
              string expressions directly from the console.
"""

import sys

from Server import *
from Filter import *

class Telnet:
    def __init__(self):
        
        self.connection = ConnectionWrapper(self)
        
    def connect(self, server='127.0.0.1', port=2100):
        self.connection.connect("127.0.0.1", int(port))
        
    def disconnect(self):
        self.connection.disconnect()
    
    def exit(self):
        self.disconnect()
        sys.exit()

    
    def send(self, message):
        self.connection.send(message)
    
    def  display(self, text, type='default'):
        print text
        
    def readConsole(self):
        try:
            while 1:
                message = raw_input()
                self.send(message)
        except:
            self.exit()
    
    def mainloop(self, server='127.0.0.1', port=19000):
    	self.connect(server, port)
    	self.readConsole()



class WrapperFilter(Filter):
    _wrapper = None
    def _init(self):
        self.wrapper = WrapperFilter._wrapper
    
    def readOut(self, data):
        self.wrapper.receive(data)
    def disconnect(self):
        self.wrapper.connection = None
        self.wrapper.receive("Disconnected", "status")

class ConnectionWrapper:
    def __init__(self, telnet):
        import thread
        
        self.telnet = telnet
        WrapperFilter._wrapper = self
        self.server = TCPServer(None,  PacketizerFilter, CompressionFilter, WrapperFilter)
        self.connection = None
        thread.start_new_thread(self.run_server, ())
    
    def connect(self, server, port, filters = []):
        if self.connection:
            self.disconnect()
        if filters:
            self.server.filters = filters
        self.connection = self.server.openConnection(server, port)
    
    def disconnect(self):
        if not self.connection:
            return False
        self.connection.end()
    
    def send(self, message):
        if not self.connection:
            return False
        self.connection.writeOut(message)
    def receive(self, message, type="default"):
        if not (str(message) == "(\"ping\")"):
            self.telnet.display(message, type)
    def run_server(self):
        try:
            self.server.run()
        except Exception, e:
            print e
    
if __name__ == "__main__":
    telnet = Telnet()
    if len(sys.argv) == 3:
        telnet.mainloop(sys.argv[1], sys.argv[2])
    else:
        telnet.mainloop()
