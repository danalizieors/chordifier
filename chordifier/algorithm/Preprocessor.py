import numpy as np

from chordifier.Keyboard import Keyboard
from chordifier.utils import axial_to_cartesian


class Preprocessor:
    def __init__(self, keyboard: Keyboard):
        self.zones = aggregate_zones(keyboard)
        self.chords = generate_chords(self.zones)
        self.positions = positions_for_chords(self.zones, self.chords)
        self.origins = define_origins(self.zones)


def aggregate_zones(keyboard):
    zones = [zone.keys for zone in keyboard.zones]
    return np.array(zones)


def generate_chords(zones):
    states = [range(zone.shape[0] + 1) for zone in zones]
    product = cartesian_product(states)
    without_first = product[1:]
    return without_first


def positions_for_chords(zones, chords):
    positions = [positions_for_chord(zones, chord) for chord in chords]
    return np.array(positions)


def positions_for_chord(zones, chord):
    zones_chord = zip(zones, chord)
    return [axial_to_cartesian(zone[button - 1])
            if 0 < button and zone.size != 0
            else np.array([np.nan, np.nan])
            for zone, button in zones_chord]


def define_origins(zones):
    origins = [axial_to_cartesian(zone[0])
               if zone.size != 0
               else np.array([np.nan, np.nan])
               for zone in zones]
    return np.array(origins)


def cartesian_product(lists):
    grid = np.meshgrid(*lists, indexing='ij')
    stacked = np.stack(grid, -1)
    return stacked.reshape(-1, len(lists))
