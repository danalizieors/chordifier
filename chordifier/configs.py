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
        'colors': (0, 9),
    },
    'index': {
        'position': vector(5, -3),
        'keys': [
            hexagon_ring(1)[0:2],
            hexagon_ring(1)[2:4],
            hexagon_ring(2)[0:2],
        ],
        'colors': (1, 8),
    },
    'middle': {
        'position': vector(6, -4),
        'keys': MIDDLE_RING_KEYS,
        'colors': (2, 7),
    },
    'ring': {
        'position': vector(7, -4),
        'keys': MIDDLE_RING_KEYS,
        'colors': (3, 6),
    },
    'little': {
        'position': vector(8, -4),
        'keys': [
            hexagon_ring(1, True)[0:2],
            hexagon_ring(1, True)[2:4],
            hexagon_ring(2, True)[0:2],
            hexagon_ring(2, True)[2:4],
        ],
        'colors': (4, 5),
    },
}

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
