#!/usr/bin/python3
"""
This is the "example" module.

The example module supplies one function, add_integer().  For example,

>>> add_integer(5, 5)
10
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int): The first integer.
    b (int, optional): The second integer. Defaults to 98.

    Returns:
    int: The sum of a and b.

    """
    result = 0

    try:
        int_a = int(a)
    except (TypeError, ValueError):
        return("a must be an integer")

    try:
        int_b = int(b)
    except (TypeError, ValueError):
        return("b must be an integer")

    return int(a + b)
