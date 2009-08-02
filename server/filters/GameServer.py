import threading
import sexpr.sexpr as sexpr

from functools import wraps
from networking.Client import AsyncClient
from filters.LogicFilter import LogicFilter
from networking.Filter import PacketizerFilter, CompressionFilter
from networking.Server import TCPServer



def runFunctionBeforeMethod(f, m):
    @wraps(m)
    def wrapper(self, *args, **kwargs):
        f(self.__class__.controller)
        return m(self, *args, **kwargs)
    return wrapper

class ServerException(Exception):
    pass

class GameFilter(LogicFilter):
    pass

class CustomizeGameFilter(type):
    def __new__(cls, name, bases, dct):
        custom = type("custom", (GameFilter, object), dict( GameFilter.__dict__,))
        custom.__init__ = runFunctionBeforeMethod(dct["message"], GameFilter.__init__)
        def setSelfToGameClass(self):
            gf = type('gf', (custom, object), dict( custom.__dict__, controller=self))
            return gf
        dct['CustomGameFilter'] = property(setSelfToGameClass)
        return type.__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        super(CustomizeGameFilter, cls).__init__(name, bases, dct)


class GameServer(object):
    """
    Contacts redirect server.
    Accepts clients
    """
    __metaclass__ = CustomizeGameFilter

    def __init__(self, user, password):
        self.client = AsyncClient()
        self.user = user
        self.password = password

    def sendToRedirect(self, l):
        self.client.send(sexpr.sexpr2str(l))

    def login(self):
        self.sendToRedirect(['login', self.user, self.password])
        if not('login-accepted' in self.client.getText()):
            raise ServerException("Could not login as %s" % self.user)

    def registerAsServer(self):
        self.sendToRedirect(['register-server'])
        if not('successful' in self.client.getText()):
            raise ServerException("Couldn't regiser as a server")

    #def startNewGame(self):
        #self.sendToRedirect([

    def runServer(self, telnet_disabled):
        filters = ([PacketizerFilter, CompressionFilter] if telnet_disabled else []) + [self.CustomGameFilter]
        self.server = TCPServer(19001,  *filters)
        server_thread = threading.Thread(None, self.server.run)
        server_thread.run()

    def run(self, telnet_disabled):
        self.client.connect(server="localhost", port=19000)
        self.login()
        self.registerAsServer()
        self.runServer(telnet_disabled)

    def message(self):
        print "Injected message before the function, called with arg", self
