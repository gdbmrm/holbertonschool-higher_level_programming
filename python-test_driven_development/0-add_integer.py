#!/usr/bin/python3
"""
The example module supplies one function, add_integer().  For example,
>>> add_integer(5, 5)
10
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    """
    result = 0

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a + b)
