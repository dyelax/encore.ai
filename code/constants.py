from os.path import join

def get_dir(directory):
    """
    Creates the given directory if it does not exist.

    @param directory: The path to the directory.
    @return: The path to the directory.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)
    return directory

CELL_SIZE = 256
NUM_LAYERS = 2

BATCH_SIZE = 50
SEQ_LEN = 25

SAMPLE_SAVE_FREQ = 100
MODEL_SAVE_FREQ =  1000

L_RATE = 0.002


# Data


SAVE_DIR = get_dir('../save/')
SAVE_NAME = 'default/'

SAMPLE_SAVE_DIR = get_dir(join(join(SAVE_DIR, 'samples'), SAVE_NAME))
MODEL_SAVE_DIR = get_dir(join(join(SAVE_DIR, 'models'), SAVE_NAME))