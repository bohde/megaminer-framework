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
import socket
import select
import threading

import Filter

class Server:
    def __init__(self):
        self.__stop = False
        self.server = False
        self.lock = threading.Lock()
        
    def run(self):
        self.__stop = False
        while not self.__stop:
            self.poll()

    def stop(self):
        self.__stop = True

    def poll(self):
        pass

class TCPServer(Server):
    def __init__(self, port, *filters):
        Server.__init__(self)
        self.filters = filters
        self.serverSocket = None
        self.sockets = []
        self.localaddr = ""
        self.setLocalAddr()
        if port:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.serverSocket.bind(('0.0.0.0', port))
            self.serverSocket.listen(5)

            self.sockets = [self.serverSocket]
        self.connections = {}

    def setLocalAddr(self):
        """
        Sets the external IP address, in case a socket returns 'localhost'
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("google.com", 0))
        self.localaddr = s.getsockname()[0]

    def poll(self):
        self.lock.acquire()
        try:
            inputReady = select.select(self.sockets, [], [])[0]
        

            for s in inputReady:
                if s == self.serverSocket:
                    ssocket, address = s.accept()
                    address = address[0]
                    if address == '127.0.0.1':
                        address = self.localaddr
                    print address
                    self.openSocket(ssocket, address, True)
    
                else:
                    try:
                        self.connections[s].poll()
                    except Exception, e:
                        raise
        except Exception, e:
            raise
        self.lock.release()


    def openConnection(self, host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        return self.openSocket(s, host)

    def openSocket(self, socket, address, server=False):
        self.sockets.append(socket)
        filters = [Filter.TCPFilter(socket)] + [i() for i in self.filters]
        for i, j in enumerate(filters[:-1]):
            j.setIn(filters[i + 1])
            j.server = server
            j.address = address
            j.master = self
        self.connections[socket] = filters[0]
        t = threading.Thread(None, filters[0].begin)
        t.start()
        return filters[-1]

    def remove(self, key):
        if key in self.connections:
            del self.connections[key]
            self.sockets.remove(key)
            return True
        return False


class SlaveTCPServer(TCPServer):
    def __init__(self, master, port, *filters):
        TCPServer.__init__(self, port, *filters)
        self.master = self.openConnection(*master)
