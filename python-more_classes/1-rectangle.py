#!/usr/bin/python3
"""
this musule creats Rectangle class
"""


class Rectangle:
    """ Rectangle blueprint """
    def __init__(self, width=0, height=0):
        " initoalasing new rectangle "
        self.width = width
        self.height = height

    @property
    def width(self):
        " get width "
        return self.__width

    @property
    def height(self):
        " get height "
        return self.__height

    @width.setter
    def width(self, value):
        " setting width "
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        " setting height "
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
