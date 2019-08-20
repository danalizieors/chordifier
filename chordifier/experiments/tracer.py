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
    'samples': 500,

    # dynamics
    'x_y_ratio': 1.5,
    'stiffness': vector(1.8, 1.3, 1.2, 1.1, 2, 2, 1.1, 1.2, 1.3, 1.8),

    # pruner
    'priority': vector(18000, 13000, 12000, 11000, 14500,
                       14516, 11008, 12004, 13002, 18001),
    'finger_priorities': 1,
    'average_offsets': 0,
    'deviation_of_offsets': 0,

    # evaluator
    'distances_travelled': 1,
    'chord_difficulties': 1,

    # optimizer
    'best': True,
    'generations': 5,
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
