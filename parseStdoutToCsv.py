from os import listdir
from os.path import isfile, join

mypath = './stdout'
outpath = './csv'
stdoutfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(stdoutfiles)

for fname in stdoutfiles:
  readFile = join(mypath, fname)
  writeFile = join(outpath, fname)
  newFile = ''
  #newFile = ','.join([str(angle) for angle in range(360)]) # header
  #newFile += '\n'
  with open(readFile) as fp:
    for line in fp:
        if line[0] == '[' and line[1] != 'I':
          newFile += line[1:-2] + '\n'
  with open(writeFile, 'w') as the_file:
    the_file.write(newFile)


