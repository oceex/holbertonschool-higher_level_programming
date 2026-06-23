#!/usr/bin/python3
"""
SQUARE ;>
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    " Square Square "
    def __init__(self, size):
        " intioalzing "
        try:
            self.integer_validator("size", size)
        except Exception as e:
            print(f"[{type(e).__name__}]", e)
        else:
            self.__size = size

    def area(self):
        " calculating the area "
        return self.__size**2

    def __str__(self):
        " stringig "
        return "[Square] {0}/{0}".format(self.__size)
