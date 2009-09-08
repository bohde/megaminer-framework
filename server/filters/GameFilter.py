from LogicFilter import LogicFilter
import statements.Statements as Statements

class GameFilter(LogicFilter):
     def _init(self):
        LogicFilter._init(self)
        self.statements = Statements.statements

