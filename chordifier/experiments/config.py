from chordifier.utils import hexagon_ring, vector

ORIGIN = [vector(0, 0)]

MIDDLE_RING_KEYS = [
    ORIGIN,
    [vector(0, -1)],
    [vector(0, 1)],
    [vector(0, -2)],
]

ZONES = {
    'thumb': {
        'position': vector(3, 0),
        'keys': [
            ORIGIN,
            hexagon_ring(1),
            hexagon_ring(2)[:-2],
            hexagon_ring(2)[-2:],
        ],
    },
    'index': {
        'position': vector(5, -3),
        'keys': [
            ORIGIN,
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
            ORIGIN,
            hexagon_ring(1, True)[0:2],
            hexagon_ring(1, True)[2:4],
            hexagon_ring(2, True)[0:2],
            hexagon_ring(2, True)[2:4],
        ],
    },
}
