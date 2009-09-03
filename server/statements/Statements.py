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
import sexpr
import random
import math
from game.match import Match
from StatementUtils import dict_wrapper, require_length, require_game
#from db import Database
#from db import Game as game_log

games = {}
id = 0
client_version = 2
statements = {}
wrapper = dict_wrapper(statements)

"""
@wrapper('request-log')
@require_length(2)
def requestLog(self, expression):
    try:
        logID = str(expression[1])
        if game_log.DB is None:
            db = Database()        
        else:
            db = game_log.DB
        self.writeSExpr(['log', logID, db.lookup_game(logID)])
        return True
    except:
        self.writeSExpr(['request-log-denied', 'Log unavailable'])
        return False
    return True
"""

@wrapper('create-game')
@require_length(1,2)
def createGame(self, expression):
    global id
    if not self.user:
        self.writeSExpr(['game-denied', 'not logged in'])
        return False
    if self.game != None:
        self.writeSExpr(['game-denied', 'already in game'])
        return False
        
    try:
        type = expression[1]
        if type not in ['zombie', 'human']:
            self.writeSExpr(['game-denied', 'invalid player type'])
            return False
    except:
        type = "human"
    
    self.type = type
    games[id] = Game.Game(id)
    games[id].addPlayer(self)
    self.game = id
    self.writeSExpr(['game-accepted', id])
    notify(self)
    id += 1
    return True

@wrapper('list-games')
@require_length(1)
def listGames(self, expression):
    #self.writeSExpr(['games', games.keys()])
    thisGame = []
    list = []
    for i in games.keys():
        thisGame = [i, games[i].listPlayers()]
        list.append(thisGame)
    self.writeSExpr(['games', list])
    return True

@wrapper('join-game')
@require_length(3)
def joinGame(self, expression):
    if not self.user:
        self.writeSExpr(['join-denied', 'not logged in'])
        return False;
    try:
        game = int(expression[1])
    except:
        game = None
    
    try:
        type = expression[2]
    except:
        type = 'player'
    if type not in ['player', 'spectator']:
        self.writeSExpr(['join-denied', 'invalid player type'])
        return False
        
    self.type = type
        
    if game not in games:
        self.writeSExpr(['join-denied', 'no such game'])
        return False
    if self.game is not None:
        self.writeSExpr(['join-denied', 'already in a game'])
        return False
    if not games[game].addPlayer(self, type):
        self.writeSExpr(['join-denied', 'game full'])
        return False
    
    self.writeSExpr(['join-accepted', type])
    self.game = game
    notify(self)
    return True

#Notify all other players of my current location.
def notify(self):
    for i in self.Connections.values():
        if not i == self:
            i.writeSExpr(['notification', self.user, games[self.game].id])

@wrapper('leave-game')
@require_length(1)
@require_game
def leaveGame(self, expression):
    games[self.game].removePlayer(self)
    self.writeSExpr(['leave-accepted'])
    if not len(games[self.game].players):
        del games[self.game]
    self.game = None
    return True

@wrapper('my-game')
@require_length(1)
def myGame(self, expression):
    self.writeSExpr(['your-game', self.game])
    return True

"""
@wrapper('game-chat')
@require_length(2)
@require_game
def gameChat(self, expression):
    games[self.game].chat(self, expression[1])
    return True
"""

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

@wrapper('game-move')
@require_length(4)
@require_game
def gameMove(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-move-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-move-denied', 'arguments not integers'])
        return False
    
    errBuff = games[self.game].move(id, x, y)
    if errBuff != True:
        self.writeSExpr(['game-move-denied', errBuff])
        return False
    return True

@wrapper('game-attack')
@require_length(4)
@require_game
def gameAttack(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-attack-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-attack-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].attack(id, x, y)
    if errBuff != True:
        self.writeSExpr(['game-attack-denied', errBuff])
        return False
    return True

@wrapper('game-build')
@require_length(5)
@require_game
def gameBuild(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-build-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
        buildingTypeID = int(expression[4])
    except:
        self.writeSExpr(['game-build-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].build(id, x, y, buildingTypeID)
    if errBuff != True:
        self.writeSExpr(['game-build-denied', errBuff])
        return False
    return True

@wrapper('game-train')
@require_length(3)
@require_game
def gameTrain(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-train-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        unitTypeID = int(expression[2])
    except:
        self.writeSExpr(['game-train-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].train(id, unitTypeID)
    if errBuff != True:
        self.writeSExpr(['game-train-denied', errBuff])
        return False
    return True

@wrapper('game-paint')
@require_length(4)
@require_game
def gameTrain(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-paint-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-paint-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].paint(id, x, y)
    if errBuff != True:
        self.writeSExpr(['game-paint-denied', errBuff])
        return False
    return True

@wrapper('game-cancel')
@require_length(2)
@require_game
def gameTrain(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-cancel-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
    except:
        self.writeSExpr(['game-cancel-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].cancel(id)
    if errBuff != True:
        self.writeSExpr(['game-cancel-denied', errBuff])
        return False
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


