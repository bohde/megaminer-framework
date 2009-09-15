from networking.Client import Client
from filters.LogicFilter import SexprHandlerMixin
from statements.Statements import require_length, dict_wrapper
from statements.StatementUtils import require_login

def protocol():
    statements = {}
    mapper = dict_wrapper(statements)

    @mapper("add")
    @require_length(2)
    def add(self, expr):
        '''
        takes an id, but how do I know what to display?
        '''
        pass

    @mapper("remove")
    @require_length(2)
    def remove(self, expr):
        pass
    
    @mapper("move")
    @require_length(4)
    def move(self, expr):
        pass

    @mapper("attack")
    @require_length(4)
    def attack(self, expr):
        pass

    @mapper("hurt")
    @requires_length(3)
    def hurt(self, expr):
        pass

    @mapper("build")
    @requires_length(4)
    def build(self, expr):
        pass

    @mapper("train")
    @requires_length(3)
    def train(self, expr):
        pass

    return statements

class VisualizerClient(Client, SexprHandlerMixin):
    """
    Glues the visualizer and protocol together
    """
    def __init__(self, *args, **kwargs):
        Client.__init__(self, *args, **kwargs)
        self.statements = protocol()

    
    
