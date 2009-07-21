import server.game.base as base


def test():
    assert False

def passtest():
    pass

def test_build_world():
    assert base.GameWorld(base.standard(10, 10)) != None
    


