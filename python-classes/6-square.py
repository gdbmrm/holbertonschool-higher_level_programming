#!/usr/bin/python3
"""
square module.
This module contains a class that defines a square.
"""


class Square:
    """
    Class that set the size of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ set the size of the square with a private attribute
        """
        self.__position = position
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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def my_print(self):
        """
        print the rectangle
        """
        if self.__size == 0:
            print()
            return

        if self.__position[1] >= 0:
            print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """
        return the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the value
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
