#!/usr/bin/python3
"""
Square module.
"""


class Square:
    """
    class Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        constructor
        """
        self.position = position
        self.size = size

    def area(self):
        """
        area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Return the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Print a square
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    @property
    def position(self):
        """
        Return the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
