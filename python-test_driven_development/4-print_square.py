#!/usr/bin/python3
""" Fonction qui affiche un carré de taille size avec des #"""


def print_square(size):
    """Crée un carré de # de taille size
    Raises:
        TypeError: if size isnt an int
        TypeError: if size is less than 0
        TypeError: if size is float or less than 0
        ZeroDivisionError: if division by zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
