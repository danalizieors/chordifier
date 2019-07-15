from chordifier.Keyboard import Keyboard


class Layout:
    def __init__(self, keyboard: Keyboard, chords: dict):
        self.keyboard = keyboard
        self.chords = chords
