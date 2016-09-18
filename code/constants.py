from os import makedirs
from os.path import join, exists

def get_dir(directory):
    """
    Creates the given directory if it does not exist.

    @param directory: The path to the directory.
    @return: The path to the directory.
    """
    if not exists(directory):
        makedirs(directory)
    return directory

CELL_SIZE = 256
NUM_LAYERS = 2

BATCH_SIZE = 50
SEQ_LEN = 5

MODEL_SAVE_FREQ =  1000

L_RATE = 0.002


# Data


SAVE_DIR = get_dir('../save/')
SAVE_NAME = 'default/'

SAMPLE_SAVE_DIR = get_dir(join(join(SAVE_DIR, 'samples'), SAVE_NAME))
MODEL_SAVE_DIR = get_dir(join(join(SAVE_DIR, 'models'), SAVE_NAME))
