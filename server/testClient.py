from filters.GameFilter import GameFilter
from statements.GameStatements import statements

def game_filter():
    """
    Use this function as if it were a filter class
    """
    gf = new GameFilter()
    gf.statements = statements
    return gf


