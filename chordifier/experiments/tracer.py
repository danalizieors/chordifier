import numpy as np
from chordifier.algorithm.Pipeline import Pipeline
from chordifier.utils import vector

STIFFNESS = vector(1.8, 1.3, 1.2, 1.1, 2)

PARAMETERS = {
    # general
    'keyboard': [3] * 3 + [0] * 7,
    'characters': 10,

    # sequencer
    'filename': "dataset/ngram.json",
    'length': 3,

    # dynamics
    'x_y_ratio': 1.5,
    'stiffness': np.hstack([STIFFNESS, STIFFNESS[::-1]]),

    # pruner
    'priority': vector(1800000, 1300000, 1200000, 1100000, 1450000,
                       1451600, 1100800, 1200400, 1300200, 1800100),
    'finger_priorities': 1,
    'average_offsets': 1,
    'deviation_of_offsets': 1,
}

pipeline = Pipeline(PARAMETERS)

pipeline.prepare()
print(pipeline.sequencer.sequences)
print(pipeline.sequencer.occurrences)
print(pipeline.sequencer.uniques)
print(pipeline.sequencer.indices)
print(pipeline.sequencer.indices[pipeline.sequencer.uniques])
