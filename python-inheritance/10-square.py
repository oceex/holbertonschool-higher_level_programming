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
            integer_validator("size", size)
        except Exception:
            pass
        else:
            self.__size = size

    def area(self):
        " calculating the area "
        return self.__size * self.__size
