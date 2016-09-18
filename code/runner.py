import tensorflow as tf
import numpy as np

import constants as c
from LSTMModel import LSTMModel
from utils import save_sample
from data_reader import DataReader


class LyricGenRunner:
    def __init__(self, model_load_path, artist_dir):
        """
        Initializes the Lyric Generation Runner.

        @param model_load_path: The path from which to load a previously-saved model.
                                Default = None.
        @param artist_dir: The directory with artist lyrics on which to train.
        """

        self.sess = tf.Session()

        ##
        # Data
        ##
        print 'Process data...'
        self.data_reader = DataReader(artist_dir)
        self.vocab = self.data_reader.get_vocab()

        print 'Init model...'
        self.model = LSTMModel(self.sess,
                               self.vocab,
                               32,
                               20,
                               1024,
                               2)

        print 'Init variables...'
        self.saver = tf.train.Saver()
        self.sess.run(tf.initialize_all_variables())

        # if load path specified, load a saved model
        if model_load_path is not None:
            self.saver.restore(self.sess, model_load_path)
            print 'Model restored from ' + model_load_path

    def train(self):
        """
        Runs a training loop on the model.
        """
        while True:
            inputs, targets = self.data_reader.get_train_batch()
            print 'Training model...'

            feed_dict = {self.model.inputs: inputs, self.model.targets: targets}
            global_step, loss, _ = self.sess.run(self.model.global_step,
                                                 self.model.loss,
                                                 self.model.optimizer,
                                                 feed_dict=feed_dict)

            if global_step % c.SAMPLE_SAVE_FREQ == 0:
                # generate and save sample sequence
                sample = self.model.generate()
                save_sample(sample, global_step)
            if global_step % c.MODEL_SAVE_FREQ == 0:
                self.saver.save(self.sess, c.MODEL_SAVE_DIR, global_step=global_step)

def main():


if __name__ == '__main__':
    main()