import numpy as np

from chordifier.Zone import Zone
from chordifier.configs import ZONES, PALETTE


class ZoneRenderer:
    def __init__(self, zone: Zone):
        self.zone = zone
        self.qs = zone.keys[:, 0]
        self.rs = zone.keys[:, 1]
        self.colors = generate_colors(zone)


def generate_colors(zone: Zone):
    color = define_color(zone)

    size = zone.keys.shape[0]
    colors = np.full(size, color)

    return colors


def define_color(zone: Zone):
    left_color, right_color = ZONES[zone.name]['colors']
    color = right_color if zone.right else left_color

    return PALETTE[color]
