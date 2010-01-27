from abc import ABCMeta

class BaseApp(object):
    __metaclass__ = ABCMeta

    def __init__(self, protocol):
        self.protocol = protocol
    
    def run(self, commands):
        def apply(coms):
            return self.__class__.mapper[coms[0]](self, coms[1:])
        return filter(bool, map(apply, commands))

class LoggingApp(BaseApp):
    pass


class AccountsApp(BaseApp):
    def __init__(self):
        self.logged_in = False
    
    def login(self, name, password):
        if name=="foo" and password=="bar":
            self.logged_in = True
            return "Success!"
        return "Failure"

    def logout(self):
        self.logged_in = False

class CompetitorsApp(BaseApp):
    pass

class GameApp(BaseApp):
    #@Protocol 
    def move(self, blah):
        return ["success"]

    
