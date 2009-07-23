from functools import wraps

def dict_wrapper(statements):
    def wrapper(string):
        def dec(f):
            statements[string] = f
            return f
        return dec
    return wrapper

def verifyLength(self, expression, *lengths):
    if len(expression) not in lengths:
        self.writeSExpr(['argument-count', expression, lengths])
        return False
    return True

def require_length(*n):
    def dec(f):
        @wraps(f)
        def wrapper(self, expression):
            if not verifyLength(self, expression, *n):
                return False
            return f(self, expression)
        return wrapper
    return dec

def require_game(f):
    @wraps(f)
    def wrapper(self, expression):
        if self.game is None:
            self.writeSExpr([expression[0]+'-denied', 'not in a game'])
            return False
        return f(self, expression)
    return wrapper
