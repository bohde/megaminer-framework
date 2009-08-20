from __future__ import with_statement
from LogicFilter import LogicFilter
import statements.RedirectStatements as RedirectStatements
import threading

class RedirectFilter(LogicFilter):
    Servers = {}
    GameNumber = 0
    Games = dict()
    GameLock = threading.Lock()



    def _init(self):
        LogicFilter._init(self)
        self.statements = RedirectStatements.statements
        self.count = 0

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
        ret = ['game-number', RedirectFilter.GameNumber, ['server'] + self.chooseServer()]
        with RedirectFilter.GameLock:
            RedirectFilter.Games[RedirectFilter.GameNumber] = ret[2]
        RedirectFilter.GameNumber += 1
        RedirectFilter.Servers[ret[2][1]].count += 1
        return ret

    def lookupGame(self, number):
        with RedirectFilter.GameLock:
            return RedirectFilter.Games[number]

    def deleteGame(self, number):
        with RedirectFilter.GameLock:
            if RedirectFilter.Servers[RedirectFilter.Games[number][1]] == self:
                del RedirectFilter.Games[number]
                self.count -= 1
                return True
            return False

