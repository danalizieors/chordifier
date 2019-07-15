import numpy as np

from chordifier.Layout import Layout


class Player:
    def __init__(self, layout: Layout):
        self.layout = layout
        self.positions = cache_positions(layout)


def cache_positions(layout):
    return {character: get_positions(buttons, layout.keyboard)
            for character, buttons in layout.chords.items()}


def get_positions(buttons, keyboard):
    buttons_zones = zip(buttons, keyboard.zones)
    positions = [zone.keys[button] if button is not None else None
                 for button, zone in buttons_zones]
    return np.array(positions)
