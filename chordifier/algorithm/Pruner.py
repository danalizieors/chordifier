import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.algorithm.Preprocessor import Preprocessor


class Pruner:
    def __init__(self, keyboard: Keyboard, parameters, prune=None):
        preprocessor = Preprocessor(keyboard)
        self.scores = score_chords(preprocessor, parameters)
        ranks = rank_chords(self.scores)

        self.zones = preprocessor.zones
        self.chords = preprocessor.chords[ranks][0:prune]
        self.positions = preprocessor.positions[ranks][0:prune]
        self.origins = preprocessor.origins


def rank_chords(scores):
    summed = np.sum(scores, axis=-1)
    return summed.argsort()


def score_chords(preprocessor, parameters):
    scores = np.array([
        finger_priorities(preprocessor.chords,
                          parameters['priority']),
        average_distances_from_origins(preprocessor.positions,
                                       preprocessor.origins,
                                       parameters['x_y_ratio'],
                                       parameters['stiffness']),
        distances_between_positions(preprocessor.positions),
    ]).T

    weights = np.array([
        parameters['finger_priorities'],
        parameters['average_distances_from_origins'],
        parameters['distances_between_positions'],
    ])

    return scores * weights


def finger_priorities(chords, priority):
    weighted = chords * priority + chords

    summed = np.sum(weighted, axis=-1)
    maximum = np.max(summed)

    return summed / maximum


def average_distances_from_origins(positions, origins, x_y_ratio, stiffness):
    offsets = positions - origins
    ratio = np.array([x_y_ratio, 1])
    weighted_offsets = offsets * ratio

    distances = np.linalg.norm(weighted_offsets, axis=-1)
    weighted_distances = distances * stiffness

    means = np.nanmean(weighted_distances, axis=-1)
    maximum = np.nanmax(means)

    return means / maximum if maximum != 0 else means


def distances_between_positions(positions):
    left = positions[:, :4]
    right = positions[:, 6:]

    distances_left = distances_between(left)
    distances_right = distances_between(right)

    distances = distances_left + distances_right
    maximum = np.max(distances)

    return distances / maximum


def distances_between(positions):
    offsets = positions[:, :-1] - positions[:, 1:]
    distances = np.linalg.norm(offsets, axis=-1)
    summed_distances = np.nansum(distances, axis=-1)
    return summed_distances
