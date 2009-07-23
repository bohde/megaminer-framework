from structures import Model, Message, Function

client = 0
server = 1

UnitType(Model):
  _name = 'UnitType'
  _key = 'id'
  id = int
  
  cost = (int, int) #base, incr
  hp = (int, int) #base, incr
  moves = int
  actions = int
  range = (int, int) #min, max
  damage = (int, int) #base, incr
  
  buildSpeed = int
  paintSpeed = int
  

class BuildingType(Model):
  _name = 'BuildingType'
  _key = 'id'
  id = int
  
  cost = (int, int) #base, incr
  hp = (int, int) #base, incr
  buildTime = (int, int, int) #base, incr
  builds = [UnitType]

class MappableObject(Model):
  _name = 'MappableObject'
  _key = 'id'
  id = int
  x = int
  y = int

class Unit(MappableObject):
  _name = 'Unit'
  type = UnitType
  level = int
  hp = int
  moves = int
  actions = int

class Buildng(MappableObject):
  _name = 'Building'
  type = BuildingType
  level = int
  hp = int

class PlayerStatus(Model):
  _name = 'PlayerStatus'
  name = str
  s

class Status(Message):
  """format: (score0 score1 (units))"""
  _head = 'Status'
  _source = server
  _format = [int, int, [Unit]]