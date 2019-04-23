import chordifier.utils as u

from chordifier.utils import hexagon_ring, vector

MIDDLE_RING_KEYS = [
    [vector(0, -1)],
    [vector(0, 1)],
    [vector(0, -2)],
]

ZONES = {
    'thumb': {
        'position': vector(3, 0),
        'keys': [
            hexagon_ring(1),
            hexagon_ring(2)[:-2],
            hexagon_ring(2)[-2:],
        ],
    },
    'index': {
        'position': vector(5, -3),
        'keys': [
            hexagon_ring(1)[0:2],
            hexagon_ring(1)[2:4],
            hexagon_ring(2)[0:2],
        ],
    },
    'middle': {
        'position': vector(6, -4),
        'keys': MIDDLE_RING_KEYS,
    },
    'ring': {
        'position': vector(7, -4),
        'keys': MIDDLE_RING_KEYS,
    },
    'little': {
        'position': vector(8, -4),
        'keys': [
            hexagon_ring(1, True)[0:2],
            hexagon_ring(1, True)[2:4],
            hexagon_ring(2, True)[0:2],
            hexagon_ring(2, True)[2:4],
        ],
    },
}


class Zone:
    def __init__(self, name, level, right=False):
        self.name = name
        self.keys = generate_keys(ZONES[name], level, right)


def generate_keys(zone, level, right):
    position = zone['position']
    keys = define_keys(zone, level)
    translated_keys = u.translate(position, keys)

    if right:
        return u.mirror(translated_keys)
    else:
        return translated_keys


def define_keys(zone, level):
    origin = vector(0, 0)
    keys = zone['keys']
    keys_for_level = keys[0:level]

    return sum(keys_for_level, [origin])
