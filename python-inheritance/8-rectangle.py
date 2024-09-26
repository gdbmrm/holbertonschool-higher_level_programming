#!/usr/bin/python3
"""
class rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry



class Rectangle(BaseGeometry):
    """
    class rectangle
    """
    def __init__(self, width, height):
        """
        initialize width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
