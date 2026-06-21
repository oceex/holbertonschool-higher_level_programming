#!/usr/bin/python3
import 7-base_geometry
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
        except Eception:
            pass
        else:
            self.__width = width
            self.__height = height

