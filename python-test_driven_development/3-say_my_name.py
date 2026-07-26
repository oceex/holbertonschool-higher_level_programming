#!/usr/bin/python3


"""
This module provides the function say_my_name(first_name, last_name="")
thats prints my name

Doctests for reading 3-say_my_name.txt:

>>> with open("tests/3-say_my_name.txt") as f:
...     f.read().strip()

"""


def say_my_name(first_name, last_name=""):
    """ prints my name saifly """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
