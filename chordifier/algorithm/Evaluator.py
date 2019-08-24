import numpy as np

from chordifier.algorithm.Pruner import Pruner
from chordifier.algorithm.Sequencer import Sequencer
from chordifier.utils import normalize_and_weight


class Evaluator:
    def __init__(self, sequencer: Sequencer, pruner: Pruner, parameters):
        self.sequencer = sequencer
        self.pruner = pruner
        self.origin_chords = repeat_origins(np.repeat(1, 10), sequencer)
        self.origin_positions = repeat_origins(self.pruner.origins, sequencer)
        self.stiffness = parameters['stiffness']
        self.weights = get_weights(parameters)

        self.pruner_permuted = None
        self.last_indices = None
        self.chords = None
        self.positions = None
        self.metrics = None
        self.scores = None
        self.totals = None
        self.occurrence_weighted = None

    def evaluate(self, permutation):
        self.prepare(permutation)
        return self.process(),

    def prepare(self, permutation):
        self.pruner_permuted = self.pruner[permutation]
        self.last_indices = self.sequencer.indices[::, -1]
        self.chords = self.generate_sequences(self.pruner_permuted.chords,
                                              self.origin_chords)
        self.positions = self.generate_sequences(self.pruner_permuted.positions,
                                                 self.origin_positions)

    def generate_sequences(self, chords, origins):
        sequences = chords[self.sequencer.indices]
        target_chords = sequences[:, [-1]]
        to_concatenate = [origins, target_chords, sequences]

        return np.concatenate(to_concatenate, axis=1)

    def process(self):
        self.metrics = self.calculate_metrics()
        previous_scores = self.pruner_permuted.scores[self.last_indices]
        new_scores = normalize_and_weight(self.metrics, self.weights)
        self.scores = np.concatenate([previous_scores, new_scores], axis=1)

        self.totals = np.sum(self.scores, axis=-1)
        self.occurrence_weighted = self.totals * self.sequencer.occurrences
        total = np.sum(self.occurrence_weighted)

        return total

    def calculate_metrics(self):
        return np.array([
            self.maximum_distances_travelled(),
            self.chord_transition_difficulties(),
        ]).T

    def maximum_distances_travelled(self):
        target_chords = self.chords[:, -1]
        target_pressed = 0 < target_chords

        source_positions = determine_source_positions(self.chords,
                                                      self.positions)
        target_positions = self.positions[:, -1]
        offsets = target_positions - source_positions

        distances = np.linalg.norm(offsets, axis=-1) * target_pressed
        weighted_distances = distances * self.stiffness

        return np.nanmax(weighted_distances, axis=-1)

    def chord_transition_difficulties(self):
        source_chords = self.chords[:, -2]
        target_chords = self.chords[:, -1]

        changed = source_chords != target_chords
        target_pressed = 0 < target_chords
        moved = changed * target_pressed

        moved_weighted = moved * self.stiffness

        return np.sum(moved_weighted, axis=-1)

    def retrieve_mapping(self, permutation):
        pruner_permuted = self.pruner[permutation]
        characters_chords = zip(self.sequencer.uniques, pruner_permuted.chords)

        return {character: chord for character, chord in characters_chords}


def determine_source_positions(chords, positions):
    without_last = chords[:, :-1]

    inverted = without_last[:, ::-1]
    pressed = 0 < inverted

    max_index = without_last.shape[-2] - 1
    first_pressed_indices = max_index - np.argmax(pressed, axis=-2)

    finger_indices = np.arange(10)
    sample_indices = np.arange(without_last.shape[0])

    pressed_positions = positions[:, first_pressed_indices, finger_indices]
    return pressed_positions[sample_indices, sample_indices]


def repeat_origins(origins, sequencer):
    samples = sequencer.indices.shape[0]
    return np.repeat([[origins]], samples, axis=0)


def get_weights(parameters):
    return np.array([
        parameters['distances_travelled'],
        parameters['chord_difficulties'],
    ])
