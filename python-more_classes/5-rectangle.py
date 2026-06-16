#!/usr/bin/python3
"""

this mudoul creats a cute rectangle

"""


class Rectangle:
    " Rectangle blueprint "
    def __init__(self, width=0, height=0):
        "  "
        self.width = width
        self.height = height

    @property
    def width(self):
        " returning width "
        return self.__width

    @property
    def height(self):
        " returning height "
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
        " calculating the area "
        return self.__width * self.__height

    def perimeter(self):
        " calculating the per "
        if self.__width and self.__height:
            return 2 (self.__width + self.__height)
        else:
            return 0

    def __str__(self):
        " printing the cute little REC "
        c = ""
        for n in range(self.__height):
            for m in range(self.__width):
                c += '#'
            if n != self.__height - 1:
                c += '\n'
       if not self.__height:
           c += '\n'

    def __repr__(self):
        " to dublecate the rectangle "
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        " To say Goodbye to my little Rec:( "
        return "Bye rectangle..."

