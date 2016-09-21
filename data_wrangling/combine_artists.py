
a_z = list(map(chr, range(97, 123)))
with open('unified_artists.txt', 'wb') as w:
  for letter in a_z:
    with open('data/' + letter + '.txt', 'r') as f:
      for extension in f.readlines():
        w.write(extension.strip() + '\n')