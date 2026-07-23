#!/usr/bin/python3


"""
This module provides the function matrix_divided(matrix, div) which returns
the div of the matrix by the div.

Doctests for reading 2-matrix_divided.txt:

>>> with open("tests/2-matrix_divided.txt") as f:
...     f.read().strip()
'hello'
"""


def matrix_divided(matrix, div):
    """ Saifly division function """
    if not all(isinstance(x, list) for x in matrix):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    m = -1
    for n in matrix:
        if not all(isinstance(x, (int, float)) for x in n):
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        if m == -1:
            m = len(n)
        else:
            if not m == len(n):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = list(map(lambda z: list(map(lambda v: round(v/div, 2), z)), matrix))
    return new


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
