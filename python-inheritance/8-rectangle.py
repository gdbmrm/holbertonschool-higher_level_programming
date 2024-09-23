#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

"""
Geometry module
"""

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        """
        initialize width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
