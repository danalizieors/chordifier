import numpy as np

from chordifier.utils import vector

PRIORITY = vector(5, 4, 3, 2, 1, 1.01, 2.01, 3.01, 4.01, 5.01)
PRIORITY = 0.1 * PRIORITY
PRIORITY = np.exp(PRIORITY)

STIFFNESS = vector(1.8, 1.3, 1.2, 1.1, 2)

PARAMETERS = {
    'keyboard': vector(3, 3, 3, 3, 2, 0, 0, 0, 0, 0),
    'priority': PRIORITY,
    'x_y_ratio': 1.5,
    'stiffness': np.hstack([STIFFNESS, STIFFNESS[::-1]]),
    'finger_priorities': 1,
    'average_distances_from_origins': 1,
    'distances_between_positions': 1,
}
