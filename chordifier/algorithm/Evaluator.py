import numpy as np

from chordifier.algorithm.Pruner import Pruner
from chordifier.algorithm.Sequencer import Sequencer


class Evaluator:
    def __init__(self, sequencer: Sequencer, pruner: Pruner, parameters):
        self.sequencer = sequencer
        self.pruner = pruner
        self.parameters = parameters
        self.origin_chords = expand_origins(np.repeat(1, 10), sequencer)
        self.origin_positions = expand_origins(self.pruner.origins, sequencer)

    def evaluate(self, permutation):
        chords, positions = self.generate_chord_position_sequences(permutation)

        scores = np.array([
            self.distances_travelled(chords, positions),
            self.chord_difficulties(chords),
        ]).T

        weights = np.array([
            self.parameters['distances_travelled'],
            self.parameters['chord_difficulties'],
        ])

        weighted_scores = scores * weights
        summed = np.sum(weighted_scores, axis=-1)

        with_occurrences = summed * self.sequencer.occurrences
        total = np.sum(with_occurrences)

        return total,

    def generate_chord_position_sequences(self, permutation):
        chords = self.generate_sequences(permutation,
                                         self.pruner.chords,
                                         self.origin_chords)
        positions = self.generate_sequences(permutation,
                                            self.pruner.positions,
                                            self.origin_positions)
        return chords, positions

    def generate_sequences(self, permutation, chords, origins):
        permuted = chords[permutation]
        sequences = permuted[self.sequencer.indices]

        target_chords = sequences[:, [-1]]
        to_concatenate = [origins, target_chords, sequences]
        return np.concatenate(to_concatenate, axis=1)

    def distances_travelled(self, chords, positions):
        source_positions = determine_source_positions(chords, positions)
        target_positions = positions[:, -1]
        offsets = target_positions - source_positions

        distances = np.linalg.norm(offsets, axis=-1)
        weighted_distances = distances * self.parameters['stiffness']

        maximums = np.nanmax(weighted_distances, axis=-1)

        return maximums

    def chord_difficulties(self, chords):
        source_chords = chords[:, -2]
        target_chords = chords[:, -1]

        changed = source_chords != target_chords
        target_pressed = 0 < target_chords
        moved = changed * target_pressed

        moved_weighted = moved * self.parameters['stiffness']

        difficulties = np.sum(moved_weighted, axis=-1)

        return difficulties

    def retrieve_mapping(self, permutation):
        permuted_chords = self.pruner.chords[permutation]
        characters_chords = zip(self.sequencer.uniques, permuted_chords)

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


def expand_origins(origins, sequencer):
    samples = sequencer.indices.shape[0]
    return np.repeat([[origins]], samples, axis=0)
