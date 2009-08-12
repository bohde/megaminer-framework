#!/usr/bin/python
# -*- coding: utf-8 -*-
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
from networking.Server import TCPServer
from networking.Filter import PacketizerFilter, CompressionFilter
import sys
import signal
from optparse import OptionParser
from filters.RedirectFilter import RedirectFilter
from filters.GameServer import GameServer

def runAsMain(f):
    def wrapper(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except KeyboardInterrupt:
            print ""
            sys.exit(0)
        except Exception, exception:
            print f.__name__, " - Unexpected error:", exception
            sys.exit(1)
        sys.exit(0)
    return wrapper


def runRedirect(telnet_disabled):
    print "Running Redirect Server.", 
    filters = ([PacketizerFilter, CompressionFilter] if telnet_disabled else []) + [RedirectFilter]
    master = TCPServer(19000,  *filters)
    print "Listening on port 19000."
    master.run()

def runGameServer(telnet_disabled):
    server = GameServer("slave", "12345")
    server.run(telnet_disabled)


def runServerAndRedirect(telnet_disabled):
    from multiprocessing import Process
    redir = Process(target=runRedirect, args=(telnet_disabled,))
    redir.start()
    server = Process(target=runGameServer, args=(telnet_disabled,))
    server.start()

def main():
    parser = OptionParser()
    parser.add_option("-r", "--redirect", action="store_true", dest="redirect", default=False)
    parser.add_option("-t", "--telnet-mode", action="store_false", dest="telnet_disabled", default=True)
    parser.add_option("-b", "--run-both", action="store_true", dest="both", default=False)
    
    (options, args) = parser.parse_args()

    runner = None
    if(options.both):
        runner = runServerAndRedirect
    else:
        runner = (runGameServer, runRedirect)[options.redirect]
    runAsMain(runner)(options.telnet_disabled)

if __name__ == "__main__":
    main()

