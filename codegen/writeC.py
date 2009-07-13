import types

from util import *

def writeClass(c, out):
  out.write("struct %s\n{\n" % (c._name,))
  for i in dir(c):
    if i[0] == '_':
      continue
    j = getattr(c, i)
    if j is int:
      out.write("  int %s;\n" % (i,))
  out.write("}\n\n")

def write(classes):
  out = file('code/models.h', 'w')
  for i in classes:
    writeClass(i, out)