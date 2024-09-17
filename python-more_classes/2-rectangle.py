#!/usr/bin/python3
"""
Rectangle module.
This module contains a class that defines a Rectangle.
"""


class Rectangle:
    """
    class that create a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        set the size of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        return the width value
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        return the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calculate the perimeter of a rectangle
        """
        perimeter = 0
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = self.__width * 2 + self.__height * 2
        return perimeter
