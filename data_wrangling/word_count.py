import os
import sys

BASE_PATH = 'artists/' + sys.argv[1] + '/'
SUM = 0
for fn in os.listdir(BASE_PATH):
  with open(BASE_PATH + fn, 'r') as f:
    SUM += len(f.read().split(' '))

print SUM