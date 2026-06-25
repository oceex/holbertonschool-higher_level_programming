#!/usr/bin/env python3
"""
Module demonstrating duck typing with an abstract Shape base class.

Defines an abstract Shape class with abstract methods `area` and
`perimeter`, two concrete implementations (Circle and Rectangle),
and a `shape_info` function that operates on any object exposing
those two methods, regardless of its actual type.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class representing a generic geometric shape.

    Subclasses must implement `area` and `perimeter`. Instantiating
    Shape directly, or a subclass missing either method, raises a
    TypeError.
    """

    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle defined by its radius.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        if radius < 0:
            self.radius = 0
        else:
            self.radius = radius

    def area(self):
        """
        Calculate the area of the circle: π * r^2.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the circumference of the circle: 2 * π * r.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle defined by its width and height.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        if width < 0 or height < 0:
            self.width = 0
            self.height = 0
        else:
            self.width = width
            self.height = height

    def area(self):
        """
        Calculate the area of the rectangle: width * height.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle: 2 * (width + height).

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a given shape object.

    Relies on duck typing: does not check the type of `shape`
    explicitly. Assumes the object implements `area()` and
    `perimeter()` methods.

    Args:
        shape: Any object implementing `area()` and `perimeter()`.

    Returns:
        None
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
