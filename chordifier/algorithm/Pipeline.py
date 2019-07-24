from chordifier.Keyboard import Keyboard
from chordifier.algorithm.Evaluator import Evaluator
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

    def prepare(self):
        self.prepare_data()
        self.prepare_keyboard()
        self.prepare_evaluator()

    def evaluate(self, permutation):
        return self.evaluator.evaluate(permutation)

    def prepare_data(self):
        self.sequencer = Sequencer(self.parameters['filename'],
                                   self.parameters['characters'],
                                   self.parameters['length'],
                                   self.parameters['samples'])

    def prepare_keyboard(self):
        self.keyboard = Keyboard(self.parameters['keyboard'])
        self.preprocessor = Preprocessor(self.keyboard)
        self.pruner_intact = Pruner(self.preprocessor, self.parameters)
        skewed = self.pruner_intact.apply_ratio(self.parameters['x_y_ratio'])
        self.pruner = skewed[0:self.parameters['characters']]

    def prepare_evaluator(self):
        self.evaluator = Evaluator(self.sequencer, self.pruner, self.parameters)
