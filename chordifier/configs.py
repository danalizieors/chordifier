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
        'palettes': (0, 9),
    },
    'index': {
        'position': vector(5, -3),
        'keys': [
            hexagon_ring(1)[0:2],
            hexagon_ring(1)[2:4],
            hexagon_ring(2)[0:2],
        ],
        'palettes': (1, 8),
    },
    'middle': {
        'position': vector(6, -4),
        'keys': MIDDLE_RING_KEYS,
        'palettes': (2, 7),
    },
    'ring': {
        'position': vector(7, -4),
        'keys': MIDDLE_RING_KEYS,
        'palettes': (3, 6),
    },
    'little': {
        'position': vector(8, -4),
        'keys': [
            hexagon_ring(1, True)[0:2],
            hexagon_ring(1, True)[2:4],
            hexagon_ring(2, True)[0:2],
            hexagon_ring(2, True)[2:4],
        ],
        'palettes': (4, 5),
    },
}

PALETTES = [
    ['#c66900', '#ff9800'],
    ['#c79100', '#ffc107'],
    ['#5a9216', '#8bc34a'],
    ['#087f23', '#4caf50'],
    ['#00675b', '#009688'],
    ['#008ba3', '#00bcd4'],
    ['#00bcd4', '#03a9f4'],
    ['#0069c0', '#2196f3'],
    ['#002984', '#3f51b5'],
    ['#320b86 ', '#673ab7'],
]
