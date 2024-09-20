#!/usr/bin/python3
"""
square module.
This module contains a class that defines a square.
"""


class Square:
    """
    Class that set the size of a square
    """
    def __init__(self, size=0):
        """ set the size of the square with a private attribute
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        return the area of a square given the size
        """
        area = self.__size ** 2
        return area

    @property
    def size(self):
        """
        return the size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of a square
        """
        self.__size = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
