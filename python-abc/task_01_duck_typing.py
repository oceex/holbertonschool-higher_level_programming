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
        self.radius = radius

    def area(self):
        " implementing abc "
        return self.radius**2 * math.pi

    def perimeter(self):
        " implementing abc "
        return self.radius * 2 * math.pi


class Rectangle(Shape):
    " defing a Rectangle "
    def __init__(self, width, height):
        " a rectangle "
        self.width = width
        self.height = height

    def area(self):
        " implementing abc "
        return self.width * self.height

    def perimeter(self):
        " implementing abc "
        return 2 * (self.width + self.height)


def shape_info(self):
    " duck typing "
    print(f"Area: {self.area()}\nPerimeter: {self.perimeter()}")
