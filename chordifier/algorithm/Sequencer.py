import numpy as np

from dataset.common import read_ngram


class Sequencer:
    def __init__(self, filename, characters, length, number=None):
        sequences_occurrences = get_ngram(filename, characters, length, number)
        self.sequences = np.array([s for s, _ in sequences_occurrences])
        self.occurrences = np.array([o for _, o in sequences_occurrences])
        self.indices, self.uniques = uniques_and_indices(self.sequences)


def get_ngram(filename, characters, length, number):
    ngram = read_ngram(filename)
    limited_characters = ngram[0:characters]
    limited_length = limited_characters.symbols(length)
    return limited_length[0:number]


def uniques_and_indices(sequences):
    uniques, indices = np.unique(sequences, return_inverse=True)
    reshaped_indices = indices.reshape(sequences.shape)

    return uniques, reshaped_indices
