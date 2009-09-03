from LogicFilter import LogicFilter
import statements.Statements as GameStatements

class GameFilter(LogicFilter):
     def _init(self):
        LogicFilter._init(self)
        self.statements = GameStatements.statements

