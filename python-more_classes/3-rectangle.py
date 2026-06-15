#!/usr/bin/python3
"""

this mudule creats Rectangle

"""


class Rectangle:
    " Rectanlge blueprint "
    def __init__(self, width=0, height=0):
        " initoalazing new Rec "
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

    def area(self):
        " calculating the Rectangle's area "
        return self.height * self.width

    def perimeter(self):
        " calculating the Rectangle's per "
        if self.height and self.width:
            return 2 * (self.height + self.width)
        return 0

    def __str__(self):
        " the Rectangle printing "
        v = ""
        for a in range(self.height):
            for b in range(self.width):
                v += '#'
            if not a == self.height - 1
                v += '\n'
        return v
