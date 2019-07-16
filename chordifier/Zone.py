import numpy as np

from chordifier.configs import ZONES


class Zone:
    def __init__(self, name: str, level: int, right: bool = False):
        self.name = name
        self.right = right
        self.keys = generate_keys(ZONES[name], level, right)


def generate_keys(zone_description: dict, level: int, right: bool):
    if level is 0:
        return np.empty((0, 2))

    position = zone_description['position']
    keys = define_keys(zone_description, level)
    translated_keys = position + keys

    return translated_keys if right else mirror(translated_keys)


def define_keys(zone_description: dict, level: int):
    possible_keys = zone_description['keys']
    keys_for_level = possible_keys[0:level]

    return np.concatenate(keys_for_level)


def mirror(coordinates):
    inverted_x = np.array([-1, 1]) * coordinates
    zeroed_y = np.array([1, 0]) * coordinates
    x_to_y = np.roll(zeroed_y, 1, 1)

    return inverted_x + x_to_y
