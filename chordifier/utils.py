import bokeh.util.hex as b
import numpy as np


def vector(*l):
    return np.array(l)


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
        return np.concatenate([ring[0:1], ring[:0:-1]])
    else:
        return ring


def walk(start, directions, steps_in_each_direction):
    current = start
    steps = []

    for direction in directions:
        for step in range(steps_in_each_direction):
            steps.append(current)
            current = current + direction

    return np.array(steps)


def axial_to_cartesian(vector):
    cartesian = b.axial_to_cartesian(vector[0], vector[1], 1, "flattop")
    return np.array(cartesian)
