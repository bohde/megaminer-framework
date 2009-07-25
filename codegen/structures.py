from copy import deepcopy as copy

class Model(object):
  data = {}
  functions = {}
  key = ''
  name = ''
  parent = None
  def __init__(self, name, **kwargs):
    self.data = {}
    self.functions = {}
    self.name = name
    if 'parent' in kwargs:
      self.parent =  kwargs['parent']
      self.data = copy(parent.data)
      self.functions = copy(parent.functions)
      self.key = parent.key
    if 'data' in kwargs:
      data = kwargs['data']
      for key, value in data.items():
        if key in self.data:
          raise ValueError('Duplicate datum %s in %s' % (key, name))
        self.data['key'] = value
    if 'functions' in kwargs:
      functions = kwargs['data']
      for key, value in functions.items():
        if key in self.functions:
          raise ValueError('Duplicate function %s in %s' % (key, name))
        self.functions['key'] = value
    if 'key' in kwargs:
      self.key = kwargs['key']

"""
TODO: Write these.
class Message(object):
  pass

class Function(object):
  arguments = None
  result = None
  
  def __init__(self, arguments, result):
    self.arguments = arguments
    self.result = result
"""