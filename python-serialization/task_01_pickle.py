#!/usr/bin/env python3
"""
module customobject
"""
import pickle


class CustomObject:
    """
    class customobject
    """
    def __init__(self, name, age, is_student):
        """
        constructor
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display name age and is student
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        serialize
        """
        try:
            with open(filename, "wb") as file_to_open:
                pickle.dump(self.name, file_to_open)
                pickle.dump(self.age, file_to_open)
                pickle.dump(self.is_student, file_to_open)
        except Exception as error:
            print(f"Error deserializing object: {error}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize
        """
        try:
            with open(filename, "rb") as file_to_open:
                student = pickle.load(file_to_open)
                return student
        except Exception as error:
            print(f"Error deserializing object: {error}")
            return None
