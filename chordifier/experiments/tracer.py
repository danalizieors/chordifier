from chordifier.algorithm.Pipeline import Pipeline
from chordifier.experiments.KeyboardFactory import make
from chordifier.utils import vector

PARAMETERS = {
    # general
    'keyboard': make([3, 3, 3, 3, 2] + [0] * 5),
    'characters': 20,

    # sequencer
    'filename': "dataset/ngram.json",
    'length': 3,
    'samples': 20,

    # dynamics
    'x_y_ratio': 1.5,
    'stiffness': vector(1.8, 1.3, 1.2, 1.1, 2, 2, 1.1, 1.2, 1.3, 1.8),

    # pruner
    'priority': vector(1800000, 1300000, 1200000, 1100000, 1450000,
                       1451600, 1100800, 1200400, 1300200, 1800100),
    'finger_priorities': 1,
    'average_offsets': 0,
    'deviation_of_offsets': 0,

    # evaluator
    'distances_travelled': 1,
    'chord_difficulties': 1,

    # optimizer
    'best': True,
    'generations': 500,
    'population_size': 100,
    'mate_probability': 0.5,
    'mutate_probability': 0.20,
    'mutate_independent_probability': 0.10,
    'select_tournament_size': 10,
}

pipeline = Pipeline(PARAMETERS)

pipeline.prepare()
result = pipeline.optimize()

print(result)
