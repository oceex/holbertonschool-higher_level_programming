#!/usr/bin/python3
"""
This module provides the function add_integer(a, b) which returns
the sum of two numbers as an integer.

Doctests for reading 0-add_integer.txt:

>>> with open("tests/0-add_integer.txt") as f:
...     f.read().strip()
'hello'
"""

def add_integer(a, b=98):
    """ Saifly Addition function """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
