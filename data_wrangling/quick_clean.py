import os

BASE_PATH = 'artists/2pac_(tupac)'
for fn in os.listdir(BASE_PATH):
  with open(BASE_PATH + '/' + fn, 'r+') as f:
    really_clean = f.read().replace('\n', ' ')
    f.write(really_clean)
