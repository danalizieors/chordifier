import numpy as np

CUBE_COORDINATE_DIRECTIONS = [
    (-1, +1),
    (0, +1),
    (+1, 0),
    (+1, -1),
    (0, -1),
    (-1, 0),
]


def hexagon_ring(radius, right=False):
    start = np.array((0, -radius))
    directions = np.array(CUBE_COORDINATE_DIRECTIONS)
    ring = walk(start, directions, radius)

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
    return np.array((-q, q + r))
