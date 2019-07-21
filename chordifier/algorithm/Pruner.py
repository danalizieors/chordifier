import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.algorithm.Preprocessor import Preprocessor


class Pruner:
    def __init__(self, keyboard: Keyboard, parameters, prune=None):
        preprocessor = Preprocessor(keyboard)
        scores = score_chords(preprocessor, parameters)
        ranks = rank_chords(scores)

        self.zones = preprocessor.zones
        self.chords = preprocessor.chords[ranks][0:prune]
        self.positions = preprocessor.positions[ranks][0:prune]
        self.origins = preprocessor.origins
        self.scores = scores[ranks][0:prune]


def rank_chords(scores):
    summed = np.sum(scores, axis=-1)
    return summed.argsort()


def score_chords(preprocessor, parameters):
    offsets = preprocessor.positions - preprocessor.origins

    scores = np.array([
        finger_priorities(preprocessor.chords,
                          parameters['priority']),
        average_offsets(offsets,
                        parameters['x_y_ratio'],
                        parameters['stiffness']),
        deviation_of_offsets(offsets),
    ]).T

    weights = np.array([
        parameters['finger_priorities'],
        parameters['average_offsets'],
        parameters['deviation_of_offsets'],
    ])

    return scores * weights


def finger_priorities(chords, priority):
    normalized_chords = np.where(0 < chords, 1, chords)
    weighted = normalized_chords * priority

    summed = np.sum(weighted, axis=-1)
    maximum = np.max(summed)

    return summed / maximum


def average_offsets(offsets, x_y_ratio, stiffness):
    ratio = np.array([x_y_ratio, 1])
    weighted_offsets = offsets * ratio

    distances = np.linalg.norm(weighted_offsets, axis=-1)
    weighted_distances = distances * stiffness

    means = np.nanmean(weighted_distances, axis=-1)
    maximum = np.max(means)

    return means / maximum if maximum != 0 else means


def deviation_of_offsets(offsets):
    deviations = np.nanstd(offsets, axis=-2)

    distances = np.linalg.norm(deviations, axis=-1)
    maximum = np.max(distances)

    return distances / maximum if maximum != 0 else distances
