import numpy as np
import os
import random

class DataReader:
  def __init__(self, artist_name):
    self.artist = artist_name
    self.lyrics = []
    self.lyric_indices = []
    self.vocab_lookup = {}

  def get_path(self):
    return os.path.join('../data/artists/', self.artist)

  # Load all song lyrics into a 2D array
  def load_lyrics(self):
    path = self.get_path()
    for fn in os.listdir(path):
      with open(os.path.join(path, fn), 'r') as song:
        self.lyrics.append(song.read().split(' '))

  # An array of unique words (work tokens) with the bottom THRESHOLD_COUNT least frequent words converted to UNK
  def get_vocab(self):
    # Load the lyric data if it hasn't been loaded already
    if len(self.lyrics) == 0:
      self.load_lyrics()

    THRESHOLD_COUNT = 10
    # Collapses the 2D array to a 1D array of words
    all_words = reduce(lambda a,b: a + b, self.lyrics)

    tokens = set(all_words)
    self.vocab_lookup = dict((word, i) for i, word in enumerate(tokens))
    self.lyric_indices = [map(lambda x: self.vocab_lookup[x], x) for x in self.lyrics]

    return list(tokens)

  def get_train_batch(self, batch_size, seq_len):
    inputs = np.empty([batch_size, seq_len], dtype=int)
    targets = np.empty([batch_size, seq_len], dtype=int)

    for i in xrange(batch_size):
      inp, target = self.get_batch(seq_len)
      inputs[i] = inp
      targets[i] = target

    return (inputs, targets)

  def get_batch(self, seq_len):
    # Pick a random song
    song = random.choice(self.lyric_indices)

    # Take a sequence of (seq_len) from the song lyrics
    i = random.randint(0, len(song) - (seq_len + 1))
    inp= np.array(song[i:i+seq_len], dtype=int)
    target =  np.array(song[i+1:i+seq_len+1], dtype=int)
    return inp, target
