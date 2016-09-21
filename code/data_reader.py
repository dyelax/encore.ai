import numpy as np
import os
import random
from collections import Counter

import constants as c

class DataReader:
    def __init__(self, artist_name):
        self.artist = artist_name
        self.lyrics = []
        self.lyric_indices = []
        self.vocab_lookup = {}

    def get_path(self):
        """
        @return: The path to the specified artist's lyric data.
        """
        return os.path.join('../data/artists/', self.artist)

    # Load all song lyrics into a 2D array
    def load_lyrics(self):
        """
        Read lyrics from file into self.lyrics - a 2D list of dimensions [songs, song_words].
        """
        path = self.get_path()
        for fn in os.listdir(path):
            with open(os.path.join(path, fn), 'r') as song:
                song_lyrics = self.clean_string(song.read()).split()
                self.lyrics.append(song_lyrics)

    def get_vocab(self):
        """
        @return: An array of unique words (tokens) with the bottom THRESHOLD_COUNT least
                 frequent words converted to '*UNK*'
        """
        # Load the lyric data if it hasn't been loaded already
        if len(self.lyrics) == 0:
            self.load_lyrics()

        # Collapses the 2D array to a 1D array of words
        all_words = reduce(lambda a,b: a + b, self.lyrics)

        # TODO: Find out why this UNK code causes differences between Linux and OS X vocabularies
        # # convert THRESHOLD_COUNT frequent words to '*UNK*'
        # THRESHOLD_COUNT = 10
        # least_referenced = Counter(all_words).most_common()[:-(THRESHOLD_COUNT + 1):-1]
        # least_referenced = [tup[0] for tup in least_referenced] # grab word from (word, count) tuple
        # print least_referenced
        #
        # self.lyrics = [map(lambda word: c.UNK if word in least_referenced else word, song)
        #                for song in self.lyrics]
        # # reset all_words to include UNKs
        # all_words = reduce(lambda a, b: a + b, self.lyrics)

        # get a sorted list of unique word tokens
        tokens = sorted(list(set(all_words)))

        # creates a map from word to index
        self.vocab_lookup = dict((word, i) for i, word in enumerate(tokens))
        # Converts words in self.lyrics to the appropriate indices.
        self.lyric_indices = [map(lambda word: self.vocab_lookup[word], song)
                              for song in self.lyrics]

        print len(tokens)

        return tokens

    def get_train_batch(self, batch_size, seq_len):
        """
        Gets a batch of sequences for training.

        @param batch_size: The number of sequences in the batch.
        @param seq_len: The number of words in a sequence.

        @return: A tuple of arrays of shape [batch_size, seq_len].
        """
        inputs = np.empty([batch_size, seq_len], dtype=int)
        targets = np.empty([batch_size, seq_len], dtype=int)

        for i in xrange(batch_size):
            inp, target = self.get_seq(seq_len)
            inputs[i] = inp
            targets[i] = target

        return inputs, targets

    def get_seq(self, seq_len):
        """
        Gets a single pair of sequences (input, target) from a random song.

        @param seq_len: The number of words in a sequence.

        @return: A tuple of sequences, (input, target) offset from each other by one word.
        """
        # Pick a random song. Must be longer than seq_len
        for i in xrange(1000):  # cap at 1000 tries
            song = random.choice(self.lyric_indices)
            if len(song) > seq_len: break

        # Take a sequence of (seq_len) from the song lyrics
        i = random.randint(0, len(song) - (seq_len + 1))
        inp= np.array(song[i:i+seq_len], dtype=int)
        target =  np.array(song[i+1:i+seq_len+1], dtype=int)
        return inp, target

    def clean_string(self, string):
        """
        Cleans unwanted characters and words from string.

        @param string: The string to be cleaned.

        @return: The cleaned string.
        """
        string = string.lower()  # lowercase

        clean_words = []
        for word in string.split():
            # clean words with quotation marks on only one side
            if word[0] == '"' and word[-1] != '"':
                word = word[1:]
            elif word[-1] == '"' and word[0] != '"':
                word = word[-1]

            # clean words with parenthases on only one side
            if word[0] == '(' and word[-1] != ')':
                word = word[1:]
            elif word[-1] == ')' and word[0] != '(':
                word = word[:-1]

            clean_words.append(word)

        return ' '.join(clean_words)

