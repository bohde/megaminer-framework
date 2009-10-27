from mako.template import Template
import glob

import structures
import conversions
import util

def write(data):
  data['conversions'] = conversions.java
  data['capitalize'] = util.capitalize
  data['lowercase'] = util.lowercase
  data['Model'] = structures.Model
  for file in glob.glob('templates/java/files/*.txt'):
    writeFile(file[21:-4], data) #file[18:-4] should strip the templates/c/files/ and .txt

def writeFile(name, data):
  template = Template(filename='templates/java/files/%s.txt' % name)
  output = file('output/java/%s' % name, 'w')
  output.write(template.render(**data))
  output.close()

if __name__ == '__main__':
  write({})
