#!/usr/bin/python3
"""
SHAPES
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    " abstract "
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    " defing a Circle "
    def __init__(self, radius):
        " a circle "
        if radius > 0:
            self.__radius = radius
        else:
            raise ValueError("radius most be positive")

    def area(self):
        " implementing abc "
        return self.__radius**2 * math.pi

    def perimeter(self):
        " implementing abc "
        return self.__radius * 2 * math.pi


class Rectangle(Shape):
    " defing a Rectangle "
    def __init__(self, width, height):
        " a rectangle "
        if width > 0 and height > 0:
            self.__width = width
            self.__height = height
        else:
            raise ValueError("width and height most be positive")

    def area(self):
        " implementing abc "
        return self.__width * self.__height

    def perimeter(self):
        " implementing abc "
        return 2 * (self.__width + self.__height)


def shape_info(self):
    " duck typing "
    are = self.area()
    per = self.perimeter()
    print(f"Area: {are}\nPerimeter: {per}")
