#!/usr/bin/python3
"""
Geometry module
"""


class BaseGeometry:

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
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
        self.__value = value
