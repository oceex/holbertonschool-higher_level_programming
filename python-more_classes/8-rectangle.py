#!/usr/bin/python3
"""

this mudule creats Rectangle

"""


class Rectangle:
    " Rectanlge blueprint "

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        " initoalazing new Rec "
        Rectangle.number_of_instances += 1
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
        " printing the cute little REC "
        c = ""
        self.print_symbol = str(self.print_symbol)
        for n in range(self.__height):
            for m in range(self.__width):
                c += self.print_symbol
            if n != self.__height - 1 and self.width:
                c += '\n'
        if not self.__height:
            c += '\n'
        return c

    def __repr__(self):
        " to dublecate the rectangle "
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        " To say Goodbye to my little Rec:( "
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        " compare between two rect's "
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, type(rect_1)):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
