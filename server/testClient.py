#!/usr/bin/python

from filters.GameFilter import GameFilter
from statements.GameStatements import statements

def game_filter():
    """
    Use this function as if it were a filter class
    """
    gf = GameFilter()
    gf.statements = statements
    return gf


if __name__ == "__main__":
    """
    run the test client
    """
    pass
