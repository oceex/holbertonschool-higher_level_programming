#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(list(map(lambda x: x * x if isinstance(x, int) else list(map(lambda w: w * w, x)), matrix)))
