#!/usr/bin/python3
from abc import ABC, abstractmethod
import math
"""
module shape
"""


class Shape(ABC):
    """
    abstract class
    """
    @abstractmethod
    def area(self):
        """
        calculate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        calculate perimeter
        """
        pass


class Circle(Shape):
    """
    class circle
    """
    def __init__(self, radius):
        """
        constructor
        """
        self.rayon = radius

    def area(self):
        """
        calculate area
        """
        return math.pi * (self.rayon ** 2)

    def perimeter(self):
        """
        calculate perimeter
        """
        return 2 * math.pi * self.rayon


class Rectangle(Shape):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        constructor
        """
        self.width = width
        self.height = height

    def area(self):
        """
        calculate area
        """
        return self.height * self.width

    def perimeter(self):
        """
        calculate perimeter
        """
        return 2 * (self.height + self.width)


def shape_info(shape):
    """
    function shape_info
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))


if __name__ == "__main__":
    circle = Circle(radius=2)
    rectangle = Rectangle(width=3, height=3)

    shape_info(circle)
    shape_info(rectangle)
