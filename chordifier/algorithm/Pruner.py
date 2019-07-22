import numpy as np
from copy import deepcopy

from chordifier.algorithm.Preprocessor import Preprocessor


class Pruner:
    def __init__(self, preprocessor: Preprocessor, parameters):
        scores = score_chords(preprocessor, parameters)
        ranks = rank_chords(scores)

        self.zones = preprocessor.zones
        self.chords = preprocessor.chords[ranks]
        self.positions = preprocessor.positions[ranks]
        self.origins = preprocessor.origins
        self.scores = scores[ranks]

    def __getitem__(self, key):
        copy = deepcopy(self)

        copy.chords = copy.chords[key]
        copy.positions = copy.positions[key]
        copy.scores = copy.scores[key]

        return copy


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
