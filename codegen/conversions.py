from util import *

import structures

import data

c = {int:'int', str:'char*'}
java = {int:'int', str:'String'}

for i in members(data):
    if isinstance(i, structures.Model):
      c[i] = '_' + i.name + '*' 
      java[i] = 'Pointer'
