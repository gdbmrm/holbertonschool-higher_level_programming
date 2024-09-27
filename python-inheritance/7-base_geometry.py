#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:
    """
    class base geometry
    with area function
    and a function that validate the integer
    """

    def area(self):
        """
        raise an exception bc area is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function that validate the value entered
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
