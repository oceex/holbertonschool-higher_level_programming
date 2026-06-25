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
        " k k "
        pass

    @abstractmethod
    def perimeter(self):
        " k k "
        pass


class Circle(Shape):
    " defing a Circle "
    def __init__(self, radius):
        " a circle "
        self.radius = abs(radius)

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
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        " implementing abc "
        return self.width * self.height

    def perimeter(self):
        " implementing abc "
        return 2 * (self.width + self.height)


def shape_info(shape):
    " duck typing "
    print(f"Area: {shape.area()}\nPerimeter: {shape.perimeter()}")
