import numpy as np
from copy import deepcopy

from chordifier.algorithm.Preprocessor import Preprocessor
from chordifier.utils import normalize_and_weight


class Pruner:
    def __init__(self, preprocessor: Preprocessor, parameters):
        skew = np.array([parameters['x_y_ratio'], 1])

        self.chords = preprocessor.chords
        self.positions = preprocessor.positions * skew
        self.origins = preprocessor.origins * skew
        self.metrics = self.calculate_metrics(parameters)
        self.scores = score_metrics(self.metrics, parameters)
        self.totals = np.sum(self.scores, axis=-1)

    def sort(self, ascending=True):
        indices_ascending = self.totals.argsort()
        indices = indices_ascending if ascending else indices_ascending[::-1]

        return self[indices]

    def __getitem__(self, key):
        copy = deepcopy(self)

        copy.chords = copy.chords[key]
        copy.positions = copy.positions[key]
        copy.metrics = copy.metrics[key]
        copy.scores = copy.scores[key]
        copy.totals = copy.totals[key]

        return copy

    def calculate_metrics(self, parameters):
        offsets = self.positions - self.origins

        return np.array([
            finger_priorities(self.chords, parameters['priority']),
            average_offsets(offsets, parameters['stiffness']),
            deviation_of_offsets(offsets),
        ]).T


def score_metrics(metrics, parameters):
    weights = np.array([
        parameters['finger_priorities'],
        parameters['average_offsets'],
        parameters['deviation_of_offsets'],
    ])

    return normalize_and_weight(metrics, weights)


def finger_priorities(chords, priority):
    pressed_fingers = 0 < chords
    weighted_fingers = pressed_fingers * priority
    return np.sum(weighted_fingers, axis=-1)


def average_offsets(offsets, stiffness):
    distances = np.linalg.norm(offsets, axis=-1)
    weighted_distances = distances * stiffness
    return np.nanmean(weighted_distances, axis=-1)


def deviation_of_offsets(offsets):
    deviations = np.nanstd(offsets, axis=-2)
    return np.linalg.norm(deviations, axis=-1)
