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

    def to_json(self, attrs=None):
        """
        return a dictionnary representation of a student
        """
        my_dict = {}
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            for i in self.__dict__.keys():
                if i in attrs:
                    my_dict[i] = getattr(self, i)
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
