from LogicFilter import LogicFilter
import statements.RedirectStatements as RedirectStatements

class RedirectFilter(LogicFilter):
    Servers = {}

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
        return [[i,j.address] for i, j in sorted(RedirectFilter.Servers.iteritems(), key=(lambda x: x[1].count))][0]