from networking.Client import AsyncClient
import threading
import sexpr.sexpr as sexpr

class GameServer(object):
    """
    Contacts redirect server.
    Accepts clients
    """
    def __init__(self):
        self.client = AsyncClient()

    def sendToRedirect(self, l):
        self.client.send(sexpr.sexpr2str(l))

    def run(self):
        t = threading.Thread(target=self.client.mainloop, kwargs={"server":"localhost", "port":19000})
        t.run()
        self.sendToRedirect(['login', 'slave', '12345'])
        t = self.client.getText()
        assert 'login-accepted' in self.client.getText()
        # Will stop if login fails.

