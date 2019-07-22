import numpy as np

from dataset.common import read_ngram


class Sequencer:
    def __init__(self, filename, characters, length):
        sequences_occurrences = setup_ngram(filename, characters, length)
        self.sequences = np.array([s for s, _ in sequences_occurrences])
        self.occurrences = np.array([o for _, o in sequences_occurrences])
        self.indices, self.uniques = uniques_and_indices(self.sequences)


def setup_ngram(filename, characters, length):
    ngram = read_ngram(filename)
    limited_ngram = ngram[0:characters]
    return limited_ngram.symbols(length)


def uniques_and_indices(sequences):
    uniques, indices = np.unique(sequences, return_inverse=True)
    reshaped_indices = indices.reshape(sequences.shape)

    return uniques, reshaped_indices
