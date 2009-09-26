from util import *

import structures

import data

c = {int:'int', str:'char*'}

for i in members(data):
    if isinstance(i, structures.Model):
      c[i] = c[i.data[i.key]]