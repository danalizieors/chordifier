from chordifier.Zone import Zone
from chordifier.configs import ZONES


class Keyboard:
    def __init__(self, zone_levels):
        self.zones = generate_zones(zone_levels)


def generate_zones(zone_levels):
    right_zone_names = list(ZONES.keys())
    left_zone_names = right_zone_names[::-1]
    zone_names = left_zone_names + right_zone_names
    is_zone_on_right = [False] * 5 + [True] * 5

    description = zip(zone_names, zone_levels, is_zone_on_right)

    return [Zone(name, level, right) for name, level, right in description]
