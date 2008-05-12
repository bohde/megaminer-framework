import sexpr.sexpr as sexpr
from config.config import getUserInfo
from networking.Filter import Filter

LOGIN_CONFIG = 'config/login.cfg'

class LogicFilter(Filter):
    ID = 0
    def _init(self, *args):
        self.user = None
        self.screenName = None
        self.password = None
        self.hash = None
        self.game = None
        self.type = None
        self.hasMap = None
        self.ID = str(LogicFilter.ID)
        LogicFilter.ID += 1
        self.run = True

    def writeSExpr(self, l):
        self.writeOut(sexpr.sexpr2str(l))

    def _readOut(self, data):
        try:
            self.readSExpr(sexpr.str2sexpr(data))
        except ValueError:
            self.writeSExpr(['malformed-message', data])

    def disconnect(self):
        self.run = False
        if self.game:
            pass
            #self.readSExpr("(leave-game)")

    def readSExpr(self, expression):
        for i in expression:
            self.evalStatement(i)

    def evalStatement(self, expression):
        if type(expression) != list:
            self.writeSExpr(['invalid-expression', expression])
            return False
        try:
            self.statements[expression[0]](self, expression)
        except Exception, e:
            print e
            self.writeSExpr(['malformed-statement', expression])

    def login(self, user, password):
        registered = False
        output = ""
        userInfo = getUserInfo(user, LOGIN_CONFIG)

        if not (userInfo is None):
            if userInfo['password'] == password:
                registered = True
                self.user = user
                self.password = password
                self.screenName = userInfo['screenName']

        if not registered:
            output = "user    :" + user + '\n'
            output += "password:" + password + '\n\n'
            outFile = open("badLogin.dat", "a")
            outFile.write(output)
            outFile.close()

        return registered

    def logout(self):
        self.user = None
        self.password = None
        self.hash = None
        return True