#!/usr/bin/python3
"""
module student
"""


class Student:
    """
    class student that define a student
    with his first and last name and his age
    """
    def __init__(self, first_name, last_name, age):
        """
        constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        return a dictionnary representation of a student
        """
        return self.__dict__
