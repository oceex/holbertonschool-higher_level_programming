#!/usr/bin/python3
"""
This module provides the function add_integer(a, b) which returns
the sum of two numbers as an integer.
"""

def add_integer(a, b=98):
    """ Saifly Addition function """
    if isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a, b = int(a), int(b)
    return a + b

