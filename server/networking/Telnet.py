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
from Server import *
from Filter import *

from Tkinter import *
import Pmw

class Telnet(Tk):
    def __init__(self, master=None):
        Tk.__init__(self, master)
        Pmw.initialise(self)
        self.title("Ubernetx0r")
        self.makeWidgets()
        
        self.connection = ConnectionWrapper(self)
        

    def makeWidgets(self):
        self.output = Pmw.ScrolledText(self)
        self.text = self.output.component("text")
        self.text.configure(state = 'disabled', background='white')
        self.text.tag_configure('echo', foreground='blue')
        self.text.tag_configure('default', foreground='black')
        self.text.tag_configure('error', foreground='red')
        self.text.tag_configure('status', foreground='green')
        self.input = Entry(self, relief=SUNKEN, background='grey')
        
        self.output.pack(side=TOP, expand=YES, fill=BOTH)
        self.input.pack(side=BOTTOM, expand=YES,  fill=BOTH)
        
        self.input.bind('<Return>', self.enterText)
        
        self.menuBar = Menu(self)
        self.fileMenu = Menu(self.menuBar, tearoff = 0)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label='Connect', command=self.connect)
        self.fileMenu.add_command(label='Disconnect', command=self.disconnect)
        self.fileMenu.add_command(label='Exit', command=self.exit)
        
        self.config(menu = self.menuBar)
        
    def enterText(self, event):
        self.send(self.input.get())
        self.input.delete(0, END)
    
    def connect(self, event=None):
        self.connection.connect("127.0.0.1", 19000)
        
    def disconnect(self, event=None):
        self.connection.disconnect()
    
    def exit(self, event=None):
        self.disconnect()
        sys.exit()

    
    def send(self, message):
        self.display(message, 'echo')
        self.connection.send(message)
    
    def  display(self, text, type='default'):
        self.text.config(state = 'normal')
        self.text.insert(END, text + '\n', type)
        self.text.config(state = 'disabled')
        self.text.see(END)



class WrapperFilter(Filter):
    def initialize(self, wrapper):
        self.wrapper = wrapper
    
    def readOut(self, data):
        print data
        self.wrapper.receive(data)
    def disconnect(self):
        self.wrapper.connection = None
        self.wrapper.receive("Disconnected", "status")

class ConnectionWrapper:
    def __init__(self, telnet):
        import thread
        
        self.telnet = telnet
        
        self.server = TCPServer(None,  PacketizerFilter(), CompressionFilter(), WrapperFilter(self))
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
        self.telnet.display(message, type)
    def run_server(self):
        try:
            self.server.run()
        except Exception, e:
            print e
    
if __name__ == "__main__":
    telnet = Telnet()
    telnet.mainloop()
    #while 1:
        #telnet.update()
        #telnet.connection.server.poll()
