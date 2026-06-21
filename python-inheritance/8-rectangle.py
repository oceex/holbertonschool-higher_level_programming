#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
finally inher
"""


class Rectangle(BaseGeometry):
    " in in "
    def __init__(self, width, height):
        " initiazi "
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except Exception:
            pass
        else:
            self.__width = width
            self.__height = height

