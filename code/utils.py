from os.path import join

import constants as c

def unkify(string, vocab):
    """
    Translates all words in string that do not appear in vocab to '*UNK*'.

    @param string: The string to be unkified.
    @param vocab: The vocabulary with respect to which we unkify.

    @return: The string, with all words unknown to the vocab translated to '*UNK*'.
    """
    words = string.split()
    for i, word in enumerate(words):
        if word not in vocab:
            words[i] = '*UNK*'

    return ''.join(words)


def save_sample(sample, step=0):
    """
    Writes sample text to file.

    @param sample: The text to write.
    @param step: The global step of training. used for file
    """
    path = join(c.SAMPLE_SAVE_DIR, str(step) + '.txt')
    with open(path, 'w') as f:
        f.write(sample)
