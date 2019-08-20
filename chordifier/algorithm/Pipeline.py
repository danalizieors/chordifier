from chordifier.algorithm.Evaluator import Evaluator
from chordifier.algorithm.Optimizer import Optimizer
from chordifier.algorithm.Preprocessor import Preprocessor
from chordifier.algorithm.Pruner import Pruner
from chordifier.algorithm.Sequencer import Sequencer


class Pipeline:
    def __init__(self, parameters: dict):
        self.parameters = parameters

        self.sequencer = None
        self.keyboard = None
        self.preprocessor = None
        self.pruner_intact = None
        self.pruner = None
        self.evaluator = None
        self.optimizer = None

    def prepare(self):
        self.prepare_sequencer()
        self.prepare_algorithm()

    def optimize(self):
        return self.optimizer.optimize()

    def prepare_sequencer(self):
        self.sequencer = Sequencer(self.parameters['filename'],
                                   self.parameters['characters'],
                                   self.parameters['length'],
                                   self.parameters['samples'])

    def prepare_algorithm(self):
        self.prepare_keyboard()
        self.prepare_pruner()
        self.prepare_evaluator()
        self.prepare_optimizer()

    def prepare_keyboard(self):
        self.keyboard = self.parameters['keyboard']
        self.preprocessor = Preprocessor(self.keyboard)

    def prepare_pruner(self):
        self.pruner_intact = Pruner(self.preprocessor, self.parameters)
        pruner_sorted = self.pruner_intact.sort(self.parameters['best'])
        self.pruner = pruner_sorted[:self.parameters['characters']]

    def prepare_evaluator(self):
        self.evaluator = Evaluator(self.sequencer, self.pruner, self.parameters)

    def prepare_optimizer(self):
        self.optimizer = Optimizer(self.evaluator, self.parameters)
