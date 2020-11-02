import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, pi
from os import listdir
from os.path import isfile, join
import random

ax = plt.subplot(111)
ax.axis('off')
def drawRays(angles, distances, color, label):
  anglesRadian = [x*2*pi/360 for x in angles]
  xs = [r*cos(theta) for theta, r in zip(anglesRadian, distances)]
  ys = [r*sin(theta) for theta, r in zip(anglesRadian, distances)]
  # for debugging print(xs, ys)
  for x,y in zip(xs, ys):
      plt.plot([0,x], [0,y], c=color, alpha=0.3, label=label)

mypath = './csv'
csvfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(csvfiles)

random_index = np.random.randint(180, size=10)

drawRays(range(360), [0.5 for i in range(360)], (0,0,1), 'boundary')

for fname, color in zip(csvfiles, [(1,0,0), (0,1,0), (0,0,1)]):
  readFile = join(mypath, fname)
  my_data = np.genfromtxt(readFile, delimiter=',')
  for i in random_index:
    start = 120
    end = 240
    drawRays(range(360)[start:end], my_data[i][start:end], color, fname)

plt.show()
