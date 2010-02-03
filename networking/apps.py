from abc import ABCMeta
from collections import defaultdict
from functools import wraps

def namedmethod(name):
    def inner(f):
        f._name = name
        f.is_protocol = True
        return f
    return inner

def protocolmethod(f):
    name = f.__name__.lower().replace("_","-")
    return namedmethod(name)(f)

class Protocol(type):
    def __new__(cls, name, bases, attrs):
        _mapper = {}
        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_protocol', 0):
                _mapper[attrvalue._name] = attrvalue
        attrs["_mapper"] = _mapper
        return super(Protocol, cls).__new__(cls, name, bases, attrs)

class BaseApp(object):
    __metaclass__ = Protocol
    wrapper = {}
    
    def __init__(self, protocol):
        self.protocol = protocol

    def run(self, commands):
        def apply(coms):
            try:
                command = self.__class__._mapper[coms[0]] 
                return command(self, *coms[1:])
            except KeyError as e:
                return "invalid-command: %s" % coms[0]
            except Exception as e:
                return "unknown-error", ("command", coms[0]), ("arguments", coms[1:])
        return filter(bool, map(apply, commands))

class LoggingApp(BaseApp):
    pass

class AccountsApp(BaseApp):
    def __init__(self):
        self.logged_in = False
        super(AccountsApp, self).__init__()
    
    def login(self, name, password):
        if name=="foo" and password=="bar":
            self.logged_in = True
        return self.logged_in

    def logout(self):
        self.logged_in = False

    def status(self):
        return self.logged_in

class CompetitorsApp(BaseApp):
    wins = defaultdict(int)
    games = defaultdict(int)

    def win(self, user):
        wins[user] += 1

    def game(self, user):
        games[user] += 1

    def user_info(self, user):
        return {"user":user,
                "wins":wins[user],
                "games":games[user]}

class GameApp(BaseApp):
    #@Protocol 
    def move(self, blah):
        return ["success"]

    
