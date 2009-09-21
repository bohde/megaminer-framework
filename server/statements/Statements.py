"""

   Copyright (C) 2008 by Steven Wallace, Ben Murrell
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
import sexpr.sexpr
import random
import math
from StatementUtils import dict_wrapper, require_length, require_game

games = {}
id = 0
client_version = 2
statements = {}
wrapper = dict_wrapper(statements)

@wrapper('game-chat')
@require_length(2)
@require_game
def gameChat(self, expression):
    games[self.game].chat(self, expression[1])
    return True

@wrapper('game-start')
@require_length(1)
@require_game
def gameStart(self, expression):
    errBuff = games[self.game].start()
    if errBuff != True:
        self.writeSExpr(['game-denied', errBuff])
        return False
    return True

@wrapper('winner')
@require_length(2)
def winner(self, expression):
    try:
        game = int(expression[1])
    except:
        game = None

    if game not in games:
        self.writeSExpr(['winner-denied', 'no such game', game])
        return False
    self.writeSExpr(['game-winner', game, games[game].winner and games[game].winner.user])
    return True

@wrapper('game-status')
@require_length(1)
@require_game
def gameStatus(self, expression):
    games[self.game].sendStatus([self])
    return True

@wrapper('end-turn')
@require_length(1)
@require_game
def endTurn(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['end-turn-denied', 'not your turn'])
        return False
    games[self.game].nextTurn()
    return True


