from functools import partial

from dataset.common import write_json

SOURCE = 'source.dat'
DESTINATION = 'ngram.json'
DEPTH = 3

MAXIMUM_OCCURRENCE_FOR_A_CHARACTER = 2 ** 32


def generate_ngram(input_filename, size):
    reader = partial(sequence_reader, size)
    ngram = {}

    with open(input_filename, encoding="utf-8", errors='ignore') as file:
        for sequence in reader(file):
            add(ngram, sequence)

    return ngram


def sequence_reader(size, file):
    sequence = read_and_next(size, file)
    while sequence:
        yield sequence
        sequence = read_and_next(size, file)


def read_and_next(size, file):
    position = file.tell()
    sequence = file.read(size)
    file.seek(position + 1)
    return sequence


def add(ngram, sequence):
    for character in sequence:
        create_or_increment_entry(ngram, character)
        ngram = ngram[character]


def create_or_increment_entry(ngram, character):
    if character not in ngram:
        ngram[character] = {
            '~~': 1
        }
    else:
        ngram[character]['~~'] += 1


def sort_ngram(ngram):
    if isinstance(ngram, dict):
        sorted_items = sorted(ngram.items(), key=item_order)
        return {key: sort_ngram(value) for key, value in sorted_items}
    else:
        return ngram


def item_order(item):
    key, value = item

    if key == '~~':
        return -MAXIMUM_OCCURRENCE_FOR_A_CHARACTER

    return -value['~~']


ngram = generate_ngram(SOURCE, DEPTH)
sorted_ngram = sort_ngram(ngram)
write_json(sorted_ngram, DESTINATION, sort=False)
