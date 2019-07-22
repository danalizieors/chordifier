import json

from dataset.Ngram import Ngram


def read_json(filename):
    with open(filename, encoding="utf-8") as file:
        return json.load(file)


def write_json(data, filename, pretty=True, sort=True):
    with open(filename, 'w', encoding="utf-8") as file:
        if pretty:
            json.dump(data, file, ensure_ascii=False, sort_keys=sort, indent=1)
        else:
            json.dump(data, file, ensure_ascii=False, sort_keys=sort,
                      separators=(',', ':'))


def read_ngram(filename):
    data = read_json(filename)
    return Ngram.parse(data)
