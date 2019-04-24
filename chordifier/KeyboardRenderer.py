import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.ZoneRenderer import ZoneRenderer


class KeyboardRenderer:
    def __init__(self, keyboard: Keyboard):
        self.keyboard = keyboard
        self.renderers = [ZoneRenderer(zone) for zone in keyboard.zones]
        self.qs = keyboard.keys[:, 0]
        self.rs = keyboard.keys[:, 1]
        self.colors = aggregate_colors(self.renderers)


def aggregate_colors(renderers):
    colors = [renderer.colors for renderer in renderers]
    return np.concatenate(colors)
