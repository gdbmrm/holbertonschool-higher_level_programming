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
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            
