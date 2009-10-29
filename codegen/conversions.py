from util import *

import structures

import data

c = {int:'int', str:'char*'}
java = {int:'int', str:'String'}
python = {int:'c_int', str:'c_char_p'}

for i in members(data):
    if isinstance(i, structures.Model):
      c[i] = '_' + i.name + '*' 
      java[i] = 'Pointer'
      python[i] = 'c_void_p'

