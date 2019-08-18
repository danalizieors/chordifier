import numpy as np

from chordifier.Models import Keyboard

PALETTE = [
    '#c66900',
    '#c79100',
    '#5a9216',
    '#087f23',
    '#00675b',
    '#008ba3',
    '#0069c0',
    '#002984',
    '#320b86',
    '#6a0080',
]


class KeyboardRenderer:
    def __init__(self, keyboard: Keyboard):
        keys = aggregate_keys(keyboard.zones)
        self.qs = keys[:, 0]
        self.rs = keys[:, 1]
        self.colors = match_colors(keyboard.zones)
        self.indices = extract_indices(keyboard.zones)
        self.positions = extract_positions(keyboard.zones)


def aggregate_keys(zones):
    return np.concatenate([zone.keys for zone in zones])


def match_colors(zones):
    zones_with_colors = zip(zones, PALETTE)
    colors = [len(zone.keys) * [color] for zone, color in zones_with_colors]
    return np.concatenate(colors)


def extract_indices(zones):
    return [index + 1 for zone in zones for index in range(len(zone.keys))]


def extract_positions(zones):
    return [key for zone in zones for key in zone.keys]
