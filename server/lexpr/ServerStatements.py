"""

   Copyright (C) 2009 by Steven Wallace, Ben Murrell
   snwallace@gmail.com, ben@benmurrell.com

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

from Statements import require_length, dict_wrapper
statements = {}
mapper = dict_wrapper(statements)

@mapper("ping")
@require_length(1)
def ping(self, expression):
    self.writeSExpr(['pong'])
    return True

@mapper("pong")
@require_length(1)
def pong(self, expression):
    return True

@mapper("login")
@require_length(3)
def login(self, expression):
    if  self.user:
        self.writeSExpr(['login-denied', 'already logged in'])
    else:
        if self.login(expression[1], expression[2]):
            self.writeSExpr(['login-accepted', 1.0])#client_version])
        else:
            self.writeSExpr(['login-denied', 'invalid username or password'])

@mapper("logout")
@require_length(1)
def logout(self, expression):
    if self.logout():
        self.writeSExpr(['logout-accepted'])
        return True
    else:
        self.writeSExpr(['logout-denied', 'not logged in'])
        return False

@mapper("whoami")
@require_length(1)
def whoAmI(self, expression):
    self.writeSExpr(['who-you-are', self.user, self.ID])
    return True

@mapper("login-accepted")
@require_length(2)
def loginAccepted(self, expression):
    print expression[1]

@mapper("malformed-statement")
def malformedStatement(self, expression):
    print expression