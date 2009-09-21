import data
import structures
from util import *

def insertModel(list, model):
  if model.parent and model.parent not in list:
    insertModel(list, model.parent)
  list.append(model)

def parseData():
  models = []
  for i in members(data):
    if isinstance(i, structures.Model):
      insertModel(models, i)
  return {'models':models}



if __name__ == '__main__':
  objects = parseData()
  import writeC
  writeC.write(objects)