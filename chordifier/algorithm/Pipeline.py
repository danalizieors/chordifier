from chordifier.algorithm.Evaluator import Evaluator
from chordifier.algorithm.Optimizer import Optimizer
from chordifier.algorithm.Preprocessor import Preprocessor
from chordifier.algorithm.Pruner import Pruner
from chordifier.algorithm.Sequencer import Sequencer


class Pipeline:
    def __init__(self, parameters: dict):
        self.parameters = parameters

        self.keyboard = parameters['keyboard']
        self.sequencer = None
        self.preprocessor = None
        self.pruner_intact = None
        self.pruner = None
        self.evaluator = None
        self.optimizer = None

    def prepare(self):
        self.prepare_data()
        self.prepare_algorithm()

    def optimize(self):
        return self.optimizer.optimize()

    def prepare_data(self):
        self.sequencer = Sequencer(self.parameters['filename'],
                                   self.parameters['characters'],
                                   self.parameters['length'],
                                   self.parameters['samples'])

    def prepare_algorithm(self):
        self.prepare_keyboard()
        self.prepare_evaluator()
        self.prepare_optimizer()

    def prepare_keyboard(self):
        self.preprocessor = Preprocessor(self.keyboard)
        self.pruner_intact = Pruner(self.preprocessor, self.parameters)
        pruned = self.pruner_intact[0:self.parameters['characters']]
        self.pruner = pruned.apply_ratio(self.parameters['x_y_ratio'])

    def prepare_evaluator(self):
        self.evaluator = Evaluator(self.sequencer, self.pruner, self.parameters)

    def prepare_optimizer(self):
        self.optimizer = Optimizer(self.evaluator, self.parameters)
