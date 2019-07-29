class Keyboard:
    def __init__(self, zones: list):
        self.zones = zones


class Zone:
    def __init__(self, keys: list, name: str, right: bool = False):
        self.keys = keys
        self.name = name
        self.right = right
