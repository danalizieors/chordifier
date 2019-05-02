from copy import deepcopy


class Ngram:
    def __init__(self, characters):
        self.characters = characters

    def __getitem__(self, key):
        copy = deepcopy(self)

        sliced = copy.characters.__getitem__(key)
        keep = set([character.symbol for character in sliced])

        for character in sliced:
            character.prune(keep)

        copy.characters = sliced

        return copy

    def limit(self, depth):
        copy = deepcopy(self)

        limit(copy, depth)

        return copy

    @staticmethod
    def parse(json):
        characters = Character.parse_list(json)
        return Ngram(characters)


class Character:
    def __init__(self, symbol, occurrences, characters):
        self.symbol = symbol
        self.occurrences = occurrences
        self.characters = characters

    def prune(self, keep):
        self.characters = [character for character in self.characters
                           if character.symbol in keep]

        for character in self.characters:
            character.prune(keep)

    @staticmethod
    def parse(json):
        symbol, properties = json
        occurrences = properties['~~']
        characters = Character.parse_list(properties)

        return Character(symbol, occurrences, characters)

    @staticmethod
    def parse_list(json):
        return [Character.parse(item)
                for item in json.items()
                if item[0] != '~~']


def limit(instance, depth):
    if depth == 0:
        instance.characters = []
    else:
        for character in instance.characters:
            limit(character, depth - 1)
