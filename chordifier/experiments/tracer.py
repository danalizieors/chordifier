import numpy as np

from chordifier.algorithm.Pipeline import Pipeline
from chordifier.utils import vector

STIFFNESS = vector(1.8, 1.3, 1.2, 1.1, 2)

PARAMETERS = {
    # general
    'keyboard': [3] * 3 + [0] * 7,
    'characters': 20,

    # sequencer
    'filename': "dataset/ngram.json",
    'length': 3,
    'samples': 20,

    # dynamics
    'x_y_ratio': 1.5,
    'stiffness': np.hstack([STIFFNESS, STIFFNESS[::-1]]),

    # pruner
    'priority': vector(1800000, 1300000, 1200000, 1100000, 1450000,
                       1451600, 1100800, 1200400, 1300200, 1800100),
    'finger_priorities': 1,
    'average_offsets': 0,
    'deviation_of_offsets': 0,

    # evaluator
    'distances_travelled': 1,
    'chord_difficulties': 1,
}

pipeline = Pipeline(PARAMETERS)

permutation = np.arange(20)
np.random.shuffle(permutation)

pipeline.prepare()
result = pipeline.evaluate(permutation)

print(result)
