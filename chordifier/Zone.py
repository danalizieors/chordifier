import numpy as np

from chordifier.configs import ZONES


class Zone:
    def __init__(self, name: str, level: int, right: bool = False):
        self.name = name
        self.right = right
        self.keys = generate_keys(ZONES[name], level, right)


def generate_keys(zone: dict, level: int, right: bool):
    position = zone['position']
    keys = define_keys(zone, level)
    translated_keys = position + keys

    if right:
        return mirror(translated_keys)
    else:
        return translated_keys


def define_keys(zone: dict, level: int):
    origin = np.array([0, 0])
    possible_keys = zone['keys']
    keys_for_level = [[origin]] + possible_keys[0:level]

    return np.concatenate(keys_for_level)


def mirror(coordinates):
    inverted_x = np.array([-1, 1]) * coordinates
    zeroed_y = np.array([1, 0]) * coordinates
    x_to_y = np.roll(zeroed_y, 1, 1)
    return inverted_x + x_to_y
