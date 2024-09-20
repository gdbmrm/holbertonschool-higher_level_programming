#!/usr/bin/python3
"""
square module.
This module contains a class that defines a square.
"""


class Square:
    """
    Class that set the size of a square
    """
    def __init__(self, size):
        """ set the size of the square with a private attribute
        """
        self.__size = size
        if isinstance(self, int):
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
