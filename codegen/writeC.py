from mako.template import Template
import glob

def write(data):
  for file in glob.glob('templates/c/files/*.txt'):
    writeFile(file[18:-4], data) #file[18:-4] should strip the templates/c/files/ and .txt

def writeFile(name, data):
  template = Template(filename='templates/c/files/%s.txt' % name)
  output = file('output/c/%s' % name, 'w')
  output.write(template.render(**data))
  output.close()

if __name__ == '__main__':
  write({})