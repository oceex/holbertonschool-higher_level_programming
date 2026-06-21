#!/usr/bin/python3
"""
finally inher
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    " in in "
    def __init__(self, width, height):
        " initiazi "
        try:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        except Exception as e:
            print(f"[{type(e).__name__}]", e)
        else:
            self.__width = width
            self.__height = height

    def area(self):
        " calculate area "
        return self.__width * self.__height

    def __str__(self):
        " printing "
        return f"[Rectangle] {self.__width}/{self.__height}"
