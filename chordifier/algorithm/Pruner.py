from itertools import product

import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.utils import axial_to_cartesian


class Pruner:
    def __init__(self, keyboard: Keyboard):
        self.keyboard = keyboard
        self.chords = generate_chords()


def prune(keyboard):
    chords = generate_chords(keyboard)
    positions = calculate_chord_positions(keyboard, chords)

    priorities = calculate_priorities(chords)
    distances_from_origin = calculate_distances_from_origin(keyboard, positions)

    return distances_from_origin


def generate_chords(keyboard):
    possible_states = [range(len(zone.keys) + 1) for zone in keyboard.zones]
    cartesian_product = product(*possible_states)

    product_array = np.array(list(cartesian_product))
    without_first = product_array[1:]
    return without_first


def calculate_chord_positions(keyboard, chords):
    positions = [chord_positions(keyboard, chord) for chord in chords]
    return np.array(positions)


def chord_positions(keyboard, buttons):
    buttons_zones = zip(buttons, keyboard.zones)
    return [axial_to_cartesian(zone.keys[button - 1])
            if 0 < button
            else (axial_to_cartesian(zone.keys[0])
                  if zone.keys.size != 0
                  else np.array([0, 0]))
            for button, zone in buttons_zones]


def calculate_priorities(chords):
    priority = np.array([5, 4, 3, 2, 1, 1.01, 2.01, 3.01, 4.01, 5.01])
    priority = 0.1 * priority
    priority = np.exp(priority)

    weighted = priority * chords

    summed = np.sum(weighted, 1)
    return summed.argsort()


def calculate_distances_from_origin(keyboard, positions):
    origins = [axial_to_cartesian(zone.keys[0])
               if zone.keys.size != 0
               else np.array([0, 0])
               for zone in keyboard.zones]

    origins_array = np.array(origins)
    offset = positions - origins_array

    return np.linalg.norm(offset, axis=2)


def distances_from_origin(keyboard, positions):
    origins = [zone.keys[0] if zone.keys.size != 0 else None
               for zone in keyboard.zones]

    return positions - origins
