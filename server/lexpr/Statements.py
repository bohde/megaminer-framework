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
import Game
from StatementUtils import dict_wrapper, require_length, require_game
from db import Database
from db import Game as game_log

games = {}
id = 0
client_version = 2
statements = {}
wrapper = dict_wrapper(statements)

@wrapper('request-log')
@require_length(2)
def requestLog(self, expression):
    #try:
        logID = str(expression[1])
        if game_log.DB is None:
            db = Database()        
        else:
            db = game_log.DB
        self.writeSExpr(['log', logID, db.lookup_game(logID)])
        return True
    #except:
        self.writeSExpr(['request-log-denied', 'Log unavailable'])
        return False
    #return True

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
        type = None
    if type not in ['zombie', 'human', 'spectator']:
        self.writeSExpr(['join-denied', 'invalid player type'])
        return False
        
    self.type = type
        
    if game not in games:
        self.writeSExpr(['join-denied', 'no such game'])
        return False
    if not games[game].addPlayer(self):
        #self.writeSExpr(['join-denied', 'game full'])
        return False
    if self.game is not None:
        self.writeSExpr(['join-denied', 'already in a game'])
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

#todo: remove
@wrapper('spectate-game')
@require_length(2)
def spectateGame(self, expression):
    if not self.user:
        self.writeSExpr(['spectate-denied', 'not logged in'])
        return False
    
    try:
        game = int(expression[1])
    except:
        game = None
    
    if game not in games:
        self.writeSExpr(['spectate-denied', 'no such game'])
        return False
    
    if not games[game].addSpectator(self):
        self.writeSExpr(['spectate-denied', 'game full'])
        return False
    
    if self.game is not None:
        self.writeSExpr(['spectate-denied', 'already in a game'])
        return False
    self.writeSExpr(['spectate-accepted'])
    self.game = game
    return True

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
    if not games[self.game].start():
        self.writeSExpr(['game-denied', 'not ready'])
        return False
    #self.writeSExpr(['game-start-accepted'])
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
@require_length(3)
@require_game
def gameAttack(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-attack-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        targetID = int(expression[2])
    except:
        self.writeSExpr(['game-attack-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].attack(id, targetID)
    if errBuff != True:
        self.writeSExpr(['game-attack-denied', errBuff])
        return False
    return True

@wrapper('game-attack-ground')
@require_length(4)
@require_game
def gameAttackGround(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-attack-ground-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-attack-ground-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].attack(id, x, y)
    if errBuff != True:
        self.writeSExpr(['game-attack-groud-denied', errBuff])
        return False
    return True

@wrapper('game-eat')
@require_length(3)
@require_game
def gameEat(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-eat-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        targetID = int(expression[2])
    except:
        self.writeSExpr(['game-eat-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].eat(id, targetID)
    if errBuff != True:
        self.writeSExpr(['game-eat-denied', errBuff])
        return False
    return True

@wrapper('game-turn')
@require_length(3)
@require_game
def gameTurn(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-turn-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        direction = int(expression[2])
    except:
        self.writeSExpr(['game-turn-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].rotate(id, direction)
    if errBuff != True:
        self.writeSExpr(['game-turn-denied', errBuff])
        return False
    return True

@wrapper('game-grab')
@require_length(3)
@require_game
def gameGrab(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-grab-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        targetID = int(expression[2])
    except:
        self.writeSExpr(['game-grab-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].grab(id, targetID)
    if errBuff != True:
        self.writeSExpr(['game-grab-denied', errBuff])
        return False
    return True

@wrapper('game-throw')
@require_length(6)
@require_game
def gameThrow(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-throw-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        itemID = int(expression[2])
        targetX = int(expression[3])
        targetY = int(expression[4])
        quantity = int(expression[5])
    except:
        self.writeSExpr(['game-throw-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].throw(id, itemID, targetX, targetY, quantity)
    if errBuff != True:
        self.writeSExpr(['game-throw-denied', errBuff])
        return False
    return True

@wrapper('game-build')
@require_length(4)
@require_game
def gameBuild(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-build-denied', 'not your turn'])
        return False
    try:
        id = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-build-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].buildWall(id, x, y)
    if errBuff != True:
        self.writeSExpr(['game-build-denied', errBuff])
        return False
    return True

#def gameCombine(self, expression):
#    if not verifyLength(self, expression, 3):
#        return False
#    if self.game == None:
#        self.writeSExpr(['game-combine-denied', 'no game'])
#        return False
#    if games[self.game].turn != self:
#        self.writeSExpr(['game-combine-denied', 'not your turn'])
#        return False
#    try:
#        id = int(expression[1])
#        target = int(expression[2])
#    except:
#        self.writeSExpr(['game-combine-denied', 'arguments not integers'])
#        return False
#
#    errBuff = games[self.game].combineUnits(id, target)
#    if errBuff != True:
#        self.writeSExpr(['game-combine-denied', errBuff])
#        return False
#    return True

@wrapper('game-human')
@require_length(4)
@require_game
def gameHuman(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-human-denied', 'not your turn'])
        return False
    try:
        x = int(expression[1])
        y = int(expression[2])
        weaponID = int(expression[3])
    except:
        self.writeSExpr(['game-human-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].spawnHuman(x, y, weaponID)
    if errBuff != True:
        self.writeSExpr(['game-human-denied', errBuff])
        return False
    return True

@wrapper('game-zombie')
@require_length(3)
@require_game
def gameZombie(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-zombie-denied', 'not your turn'])
        return False
    try:
        spawnZoneID = int(expression[1])
        facing = int(expression[2])
    except:
        self.writeSExpr(['game-zombie-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].spawnZombie(spawnZoneID, facing)
    if errBuff != True:
        self.writeSExpr(['game-zombie-denied', errBuff])
        return False
    return True

@wrapper('game-airstrike')
@require_length(4)
@require_game
def gameAirstrike(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-airstrike-denied', 'not your turn'])
        return False
    try:
        itemID = int(expression[1])
        x = int(expression[2])
        y = int(expression[3])
    except:
        self.writeSExpr(['game-airstrike-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].callAirstrike(x, y, itemID)
    if errBuff != True:
        self.writeSExpr(['game-airstrike-denied', errBuff])
        return False
    return True

@wrapper('game-give')
@require_length(4)
@require_game
def gameGive(self, expression):
    if games[self.game].turn != self:
        self.writeSExpr(['game-give-denied', 'not your turn'])
        return False
    try:
        giverID = int(expression[1])
        takerID = int(expression[2])
        quantity = int(expression[3])
    except:
        self.writeSExpr(['game-give-denied', 'arguments not integers'])
        return False

    errBuff = games[self.game].giveAmmo(giverID, takerID, quantity)
    if errBuff != True:
        self.writeSExpr(['game-give-denied', errBuff])
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

