import numpy as np

from chordifier.Models import Keyboard, Zone
from chordifier.experiments.config import ZONES


def make(zone_levels):
    zones = generate_zones(zone_levels)
    return Keyboard(zones)


def generate_zones(zone_levels):
    right_zone_names = list(ZONES.keys())
    left_zone_names = right_zone_names[::-1]
    zone_names = left_zone_names + right_zone_names
    is_zone_on_right = [False] * 5 + [True] * 5

    zone_descriptions = zip(zone_names, zone_levels, is_zone_on_right)

    return [generate_zone(*description) for description in zone_descriptions]


def generate_zone(name, level, right):
    zone_description = ZONES[name]
    keys = generate_keys(zone_description, level, right)

    return Zone(keys, name, right)


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
