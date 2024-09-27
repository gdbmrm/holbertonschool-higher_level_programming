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
        self.__rayon = radius

    def area(self):
        """
        calculate area
        """
        return pi * self.__rayon ** 2

    def perimeter(self):
        """
        calculate perimeter
        """
        return 2 * pi * self.__rayon


class Rectangle(Shape):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        constructor
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        calculate area
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        calculate perimeter
        """
        return self.__height * 2 + self.__width * 2


def shape_info(shape):
    """
    function shape_info
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))


circle = Circle(radius=2)
rectangle = Rectangle(width=3, height=3)

shape_info(circle)
shape_info(rectangle)
