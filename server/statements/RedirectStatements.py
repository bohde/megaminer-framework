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
from StatementUtils import require_login
statements = {}
mapper = dict_wrapper(statements)

@mapper("ping")
@require_length(1)
def ping(self, expression):
    self.writeSExpr(['pong'])
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
    self.writeSExpr(['who-you-are', ['id', self.ID], ['address', self.address]])
    return True

@mapper('register-server')
@require_length(1)
@require_login
def registerServer(self, expression):
    self.registerAsServer()
    self.writeSExpr(['registered-status', 'successful'])
    return True

@mapper('list-servers')
@require_length(1)
@require_login
def listServers(self, expression):
    self.writeSExpr(['servers', self.getServers()])
    return True

@mapper('get-server')
@require_length(1)
@require_login
def getServer(self, expression):
    self.writeSExpr(["server"] + self.chooseServer())
    return True

@mapper('start-game')
@require_length(1)
@require_login
def startGame(self, expression):
    self.writeSExpr(self.createGame())
    return True

@mapper('join-game')
@require_length(2)
@require_login
def joinGame(self, expression):
    try:
        self.writeSExpr(self.lookupGame(int(expression[1])))
        return True
    except:
        self.writeSExpr(['join-game-denied', ['invalid-number', expression[1]]])
    
@mapper('end-game')
@require_length(2)
@require_login
def endGame(self, expression):
    try:
        if self.deleteGame(int(expression[1])):
            self.writeSExpr(['game-ended', int(expression[1])])
            return
    except:
        pass
    self.writeSExpr(['end-game-denied', ['invalid-number', expression[1]]])


