import types

import structures

from util import *

def writeClass(c, out):
  if c.__bases__[0] == structures.Model:
    parent = "object"
  else:
    parent = c.__bases__[0]._name
  out.write("class %s(%s):\n" % (c._name, parent))
  #write all the members
  for i in dir(c):
    if i[0] == '_':
      continue
    j = getattr(c, i)
    if j is int:
      out.write("  %s = 0\n" % (i,))
  #then the functios
  out.write("\n")
  writeToList(c, out)
  out.write("\n")
  writeFromList(c, out)
  out.write("\n")

#writes the function to store the class in a list
def writeToList(c, out):
  out.write("  toList(self):\n")
  out.write("    return (")
  for i in dir(c):
    if i[0] == '_':
      continue
    j = getattr(c, i)
    if j in (int,):
      out.write("%s," % (i,))
  out.write(")\n")

#writes the function to retrieve the class from a list
def writeFromList(c, out):
  out.write("  fromList(self, list):\n")
  index = 0 #index in the list
  for i in dir(c):
    if i[0] == '_':
      continue
    j = getattr(c, i)
    if j in (int,):
      out.write("    %s = list[%s]\n" % (i, index))
    index += 1

def write(classes):
  out = file('code/models.py', 'w')
  for i in classes:
    writeClass(i, out)