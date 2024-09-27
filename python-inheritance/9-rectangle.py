#!/usr/bin/python3
"""
Geometry module
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class rectangle with an str function and an area function
    """
    def __init__(self, width, height):
        """
        initialize width and height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        print [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        return the area of the rectangle
        """
        return self.__width * self.__height
