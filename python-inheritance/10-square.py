#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    childclass square
    """
    def __init__(self, size):
        """
        constructeur
        """
        super().integer_validator("carré", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        return the area of the square
        """
        return self.__size ** 2
