import numpy as np


def vector(x, y):
    return np.array([x, y])


CUBE_COORDINATE_DIRECTIONS = [
    vector(-1, +1),
    vector(0, +1),
    vector(+1, 0),
    vector(+1, -1),
    vector(0, -1),
    vector(-1, 0),
]


def hexagon_ring(radius, right=False):
    start = vector(0, -radius)
    ring = walk(start, CUBE_COORDINATE_DIRECTIONS, radius)

    if right:
        return ring[0:1] + ring[:0:-1]
    else:
        return ring


def walk(start, directions, steps_in_each_direction):
    current = start
    steps = []

    for direction in directions:
        for step in range(steps_in_each_direction):
            steps.append(current)
            current = current + direction

    return steps


def translate(position, coordinates):
    return [position + coordinate for coordinate in coordinates]


def mirror(coordinates):
    return [mirror_coordinate(coordinate) for coordinate in coordinates]


def mirror_coordinate(coordinate):
    q, r = coordinate
    return vector(-q, q + r)
