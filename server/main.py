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
from optparse import OptionParser
from filters.RedirectFilter import RedirectFilter


def runRedirect(telnet_disabled):
    try:
        print "Running Redirect Server.", 
        filters = ([PacketizerFilter, CompressionFilter] if telnet_disabled else []) + [RedirectFilter]
        master = TCPServer(19000,  *filters)
        print "Listening on port 19000."
        master.run()
    except Exception, exception:
        print "runRedirect - Unexpected error:", exception
        sys.exit(1)
    sys.exit(0)

def runGameServer(telnet_disabled):
    raise NotImplementedError("Game server is not yet implemented.")

def main():
    parser = OptionParser()
    parser.add_option("-r", "--redirect", action="store_true", dest="redirect", default=False)
    parser.add_option("-t", "--telnet-mode", action="store_false", dest="telnet_disabled", default=True)

    (options, args) = parser.parse_args()

    (runGameServer, runRedirect)[options.redirect](options.telnet_disabled)

if __name__ == "__main__":
    main()

