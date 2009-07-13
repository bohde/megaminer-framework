class Model(object):
  pass

class Message(object):
  pass

class Function(object):
  arguments = None
  result = None
  
  def __init__(self, arguments, result):
    self.arguments = arguments
    self.result = result
