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
from game.match import Match
from StatementUtils import dict_wrapper, require_length, require_game, \
                           require_login

games = {}
id = 0
client_version = 2
statements = {}
wrapper = dict_wrapper(statements)

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

@wrapper('create-game')
@require_length(2)
def createGame(self, expression):
    try:
        game = int(expression[1])
    except:
        self.writeSExpr(['create-game-denied', 'invalid game number'])
        return False

    print "Creating game " + str(game)

    if games.get(game, None) is not None:
        self.writeSExpr(['create-game-denied', 'game number already exists'])

    games[game] = Match(game)

    return True

@wrapper('join-game')
@require_login
@require_length(2, 3)
def joinGame(self, expression):
    try:
        game = int(expression[1])
    except:
        game = None

    try:
        type = str(expression[2])
    except:
        type = "player"

    if game not in games:
        self.writeSExpr(['join-game-denied', 'no such game', game])
        return False

    errBuff = games[game].addPlayer(self, type)

    if errBuff != True:
        self.writeSExpr(['join-game-denied', errBuff])
        return False

    self.game = game

    return True
