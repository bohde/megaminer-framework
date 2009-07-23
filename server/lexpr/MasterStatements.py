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
wrapper = dict_wrapper(statements)

@wrapper("server-login")
@require_length(3)
def serverLogin(self, expression):
    if  self.server or self.user:
        self.writeSExpr(['login-denied', 'already logged in'])
    else:
        if self.login(expression[1], expression[2]):
            self.writeSExpr(['login-accepted', 1.0])#client_version])
        else:
            self.writeSExpr(['login-denied', 'invalid username or password'])

#@wrapper("finish-game")
#@require_length(2)
#def finishGame(self, expression):
     #if self.server:
        #self.

