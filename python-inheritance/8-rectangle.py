#!/usr/bin/python3
"""
finally inher
"""


class BaseGeometry:
    "the baasee "
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        " int "
        if not isinstance(value, int) or value.__class__ == bool:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    " in in "
    def __init__(self, width, height):
        " initiazi "
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except Eception:
            pass
        else:
            self.__width = width
            self.__height = height

