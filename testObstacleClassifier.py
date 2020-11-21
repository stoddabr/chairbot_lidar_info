import numpy as np
from math import sin, cos, pi
from os import listdir
from os.path import isfile, join

def sequenceNumbers(l):
  res = [[l[0]]]

  for i in range(0,len(l)-1):

    if (l[i])==(l[i+1]-1):
      res[-1].append((l[i+1]))
    else:
      res.append([l[i+1]])

  return res

def objDetection(dataInput, objMinSiz_deg = 5, d_m=1.5):
  #sort out data points
  idx = [i for i, x in enumerate(dataInput) if (x < 0.75 and x > 0)]

  #evaluate objects based on size
  obstacles = []
  if len(idx)>0:
    seqs = sequenceNumbers(idx)
    for s in range(0, len(seqs) - 1):
      if len(seqs[s]) > objMinSiz_deg:
        obstacles.append(seqs[s])

  #create output dict
  obstDict = {}
  if len(obstacles)>0:
    for i in range(0, len(obstacles)):
      deg2obj_deg = sum(obstacles[i])/len(obstacles[i])
      d2obj_m = dataInput[int(round(deg2obj_deg))]
      obstDict[str(int(round(deg2obj_deg)))] = [deg2obj_deg, d2obj_m, obstacles[i], dataInput[obstacles[i]]]

  return obstDict

def classifyLidar(data):
  ''' returns true if obstacle, false otherwise, data is array '''
  # TODO Mark, your code here
  detectionRes = objDetection(data)
  return bool(detectionRes)


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
