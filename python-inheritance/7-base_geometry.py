#!/usr/bin/python3
"""
improve
"""


class BaseGeometry:
    "the baasee "
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        " int "
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
