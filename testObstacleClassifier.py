import numpy as np
from math import sin, cos, pi
from os import listdir
from os.path import isfile, join


def classifyLidar(data):
  ''' returns true if obstacle, false otherwise, data is array '''
  # TODO Mark, your code here
  return False

mypath = './csv'
csvfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
samples = [] # array of (label, array data)
rate = 0.05 # % of data in sample, higher will return more samples, range 0-1

for fname in csvfiles:
  readFile = join(mypath, fname)
  with open(readFile) as fp:
    for line in fp:
      if np.random.random() < rate:
        data = np.array(line[:-1].split(',')).astype(float)
        samples.append((fname, data))

correct = 0
wrong = 0
for label, data in samples:
  result = classifyLidar(data)
  fileIndex = int(result)
  guess = csvfiles[fileIndex]
  if guess == label:
    correct += 1
  else:
    wrong += 1

print('number correct: ', correct)
print('number wrong: ', wrong)
print('accuracy: ', float(correct)/float(wrong+correct) )
