from os import makedirs
from os.path import join, exists

##
# Network
##

# Size of LSTM cell hidden states and word embeddings.
CELL_SIZE = 256
# Number of LSTM layers
NUM_LAYERS = 2

##
# Training
##

# Learning rate for training.
L_RATE = 0.002
# Number of sequences in a training batch.
BATCH_SIZE = 50
# Length of sequence to train on,
# eg., seq_len=5 => inputs='The quick brown fox jumps', targets='quick brown fox jumps over'.
SEQ_LEN = 5

##
# Data
##

def get_dir(directory):
    """
    Creates the given directory if it does not exist.

    @param directory: The path to the directory.
    @return: The path to the directory.
    """
    if not exists(directory):
        makedirs(directory)
    return directory

def set_save_name(name):
    """
    Edits all constants dependent on SAVE_NAME.

    @param name: The new save name.
    """
    global SAVE_NAME, MODEL_SAVE_DIR

    SAVE_NAME = name
    MODEL_SAVE_DIR = get_dir(join(SAVE_DIR, 'models/', SAVE_NAME))


# Directory in which to save content
SAVE_DIR = get_dir('../save/')
# subdirectory of SAVE_DIR/* to differentiate between runs/models.
SAVE_NAME = 'default/'
# Directory in which to save trained models.
MODEL_SAVE_DIR = get_dir(join(join(SAVE_DIR, 'models'), SAVE_NAME))

# How often to save the model, in # steps.
MODEL_SAVE_FREQ = 5000

##
# Misc
##

# Token for rare words in the vocabulary, used to simulate unknown seed words.
UNK = '*UNK*'
