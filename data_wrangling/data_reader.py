import numpy as np
import os
from collections import Counter

class DataReader:
  def __init__(self, artist_name):
    self.artist = artist_name
    self.lyrics = []

  def get_path(self):
    return 'artists/' + self.artist + '/'

  # Load all song lyrics into a 2D array
  def load_lyrics(self):
    path = self.get_path()
    for fn in os.listdir(path):
      with open(path + fn, 'r') as song:
        self.lyrics.append(song.read().split(' '))

  # An array of unique words (work tokens) with the bottom THRESHOLD_COUNT least frequent words converted to UNK
  def get_vocab(self):
    # Load the lyric data if it hasn't been loaded already
    if len(self.lyrics) == 0:
      self.load_lyrics()

    THRESHOLD_COUNT = 10
    # Collapses the 2D array to a 1D array of words
    all_words = reduce(lambda a,b: a + b, self.lyrics)

    c = Counter(all_words)
    least_common_words = c.most_common()[:-20]
    print least_common_words


  def get_train_batch(batch_size, seq_size):
    inputs
    targets
    pass
    return (inputs, targets)


dr = DataReader('kanye_west')
dr.get_vocab()