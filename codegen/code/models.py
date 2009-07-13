class Building(MappableObject):
  hp = 0
  id = 0
  x = 0
  y = 0

  toList(self):
    return (hp,id,x,y,)

  fromList(self, list):
    hp = list[0]
    id = list[1]
    x = list[2]
    y = list[3]

class MappableObject(object):
  id = 0
  x = 0
  y = 0

  toList(self):
    return (id,x,y,)

  fromList(self, list):
    id = list[0]
    x = list[1]
    y = list[2]

class Unit(MappableObject):
  actions = 0
  hp = 0
  id = 0
  maxactions = 0
  maxmoves = 0
  moves = 0
  x = 0
  y = 0

  toList(self):
    return (actions,hp,id,maxactions,maxmoves,moves,x,y,)

  fromList(self, list):
    actions = list[0]
    hp = list[1]
    id = list[2]
    maxactions = list[3]
    maxmoves = list[4]
    moves = list[5]
    x = list[6]
    y = list[7]

