from networking.Server import *
from networking.Filter import *

import os

import sys, traceback

ID = 0


class FileServerFilter(Filter):
    def initialize(self, *args):
        self.file = None
    
    def readOut(self, data):
    	#print data BAD!
    	try:
            lines = data.split("\n")
            f = "./clients/" + lines[0]
            data = "\n".join(lines[1:])
            if f == "ctypes" or f == "jna.jar":
                print "Someone is being an asshole"
                return
            file(f, 'wb').write(data)
            os.system("chmod +x " + f)
        except:
            traceback.print_exc(file=sys.stdout)

    def writeOut(self, data):
        Filter.writeOut(self, data)        

    def disconnect(self):
        print "disconnect"
        

server = TCPServer(18000, PacketizerFilter, FileServerFilter)
server.run()
