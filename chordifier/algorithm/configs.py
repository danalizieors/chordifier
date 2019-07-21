import numpy as np

from chordifier.utils import vector

STIFFNESS = vector(1.8, 1.3, 1.2, 1.1, 2)

PARAMETERS = {
    'keyboard': vector(3, 3, 3, 3, 2, 0, 0, 0, 0, 0),
    'priority': vector(1800000, 1300000, 1200000, 1100000, 1450000,
                       1451600, 1100800, 1200400, 1300200, 1800100),
    'x_y_ratio': 1.5,
    'stiffness': np.hstack([STIFFNESS, STIFFNESS[::-1]]),
    'finger_priorities': 1,
    'average_offsets': 1,
    'deviation_of_offsets': 1,
}
