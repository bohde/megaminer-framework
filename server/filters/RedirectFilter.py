from __future__ import with_statement
from LogicFilter import LogicFilter
import statements.RedirectStatements as RedirectStatements
import threading

class RedirectFilter(LogicFilter):
    Servers = {}

    def _init(self):
        LogicFilter._init(self)
        self.statements = RedirectStatements.statements
        self.count = 0
        self.game_number = 0
        self.games = dict()
        self.game_lock = threading.Lock()

    def disconnect(self):
        if self.ID:
            try:
                del RedirectFilter.Servers[self.ID]
            except Exception:
                pass
            self.ID = None
        LogicFilter.disconnect(self)

    def registerAsServer(self):
        RedirectFilter.Servers[self.ID] = self

    def getServers(self):
        return [[i, j.address] for i,j in RedirectFilter.Servers.iteritems()]

    def chooseServer(self):
        ret = [[i,j.address] for i, j in sorted(RedirectFilter.Servers.iteritems(), key=(lambda x: x[1].count))]
        return [[], ret[0]][len(ret)>0]

    def createGame(self):
        ret = ['game-number', self.game_number, ['server'] + self.chooseServer()]
        with self.game_lock:
            self.games[self.game_number] = ret[2]
        self.game_number += 1
        return ret

    def lookupGame(self, number):
        with self.game_lock:
            return self.games[number]

    def deleteGame(self, number):
        with self.game_lock:
            del self.games[number]

