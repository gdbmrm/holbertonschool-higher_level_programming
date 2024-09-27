#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi
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
        return pi * self.rayon ** 2

    def perimeter(self):
        """
        calculate perimeter
        """
        return 2 * pi * self.rayon


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
        return self.height * 2 + self.width * 2


def shape_info(shape):
    """
    function shape_info
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))


if __name__ == "__main__":
    circle = Circle(radius=2)
    rectangle = Rectangle(width=3, height=3)

    shape_info(circle)
    shape_info(rectangle)
