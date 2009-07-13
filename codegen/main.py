import types
import data
from util import *

def parseModels():
  for i in members(data):
    if type(i) == types.TypeType and issubclass(i, data.Model) and i is not data.Model:
      yield i



if __name__ == '__main__':
  objects = [i for i in parseModels()]
  import writeC
  writeC.write(objects)
  import writeServerPy
  writeServerPy.write(objects)