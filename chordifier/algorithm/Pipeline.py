from chordifier.Keyboard import Keyboard
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
        self.mapping = None

    def prepare(self):
        self.prepare_data()
        self.prepare_keyboard()

    def evaluate(self):
        print('evaluating')

    def prepare_data(self):
        self.sequencer = Sequencer(self.parameters['filename'],
                                   self.parameters['characters'],
                                   self.parameters['length'])

    def prepare_keyboard(self):
        self.keyboard = Keyboard(self.parameters['keyboard'])
        self.preprocessor = Preprocessor(self.keyboard)
        self.pruner_intact = Pruner(self.preprocessor, self.parameters)
        self.pruner = self.pruner_intact[0:self.parameters['characters']]
