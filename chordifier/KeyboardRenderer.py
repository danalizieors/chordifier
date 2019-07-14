import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.configs import PALETTE


class KeyboardRenderer:
    def __init__(self, keyboard: Keyboard):
        keys = aggregate_keys(keyboard.zones)
        self.qs = keys[:, 0]
        self.rs = keys[:, 1]
        self.colors = match_colors(keyboard.zones)


def aggregate_keys(zones):
    return np.concatenate([zone.keys for zone in zones])


def match_colors(zones):
    zones_with_colors = zip(zones, PALETTE)
    colors = [len(zone.keys) * [color] for zone, color in zones_with_colors]
    return np.concatenate(colors)
