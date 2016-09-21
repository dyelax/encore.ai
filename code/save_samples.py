"""
Save a bunch of random samples of each of our models to put up on the website while we figure out
how to host the actual TensorFlow models.
"""

import tensorflow as tf
from os.path import join
import getopt
import sys

from LSTMModel import LSTMModel
from data_reader import DataReader
import constants as c

def process_sample(string):
    words = string.split()

    #remove everything before the first line break
    words = words[words.index('*break*'):]

    #remove opening line breaks
    while words[0] == '*break':
        words = words[1:]

    newString = ' '.join(words)

    newString = newString.replace('*break*', '\n')
    return newString

def save(artist, model_path, num_save):
    sample_save_dir = c.get_dir('../save/samples/')
    sess = tf.Session()

    print artist

    data_reader = DataReader(artist)
    vocab = data_reader.get_vocab()

    print 'Init model...'
    model = LSTMModel(sess,
                      vocab,
                      c.BATCH_SIZE,
                      c.SEQ_LEN,
                      c.CELL_SIZE,
                      c.NUM_LAYERS,
                      test=True)

    saver = tf.train.Saver()
    sess.run(tf.initialize_all_variables())

    saver.restore(sess, model_path)
    print 'Model restored from ' + model_path

    artist_save_dir = c.get_dir(join(sample_save_dir, artist))
    for i in xrange(num_save):
        print i

        path = join(artist_save_dir, str(i) + '.txt')
        sample = model.generate()
        processed_sample = process_sample(sample)

        with open(path, 'w') as f:
            f.write(processed_sample)


def main():
    artist = 'kanye_west'
    model_path = '../save/models/kanye_west/kanye_west.ckpt-30000'
    num_save = 1000

    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'l:a:N:', ['load_path=', 'artist_name=', 'num_save='])
    except getopt.GetoptError:
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-l', '--load_path'):
            model_path = arg
        if opt in ('-a', '--artist_name'):
            artist = arg
        if opt in ('-n', '--num_save'):
            num_save = int(arg)

    save(artist, model_path, num_save)

if __name__ == '__main__':
    main()