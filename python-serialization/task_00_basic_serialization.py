#!/usr/bin/env python3
"""
module basic serialization
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    serialize and save data to the specified file
    """
    with open(filename, "wb") as file_to_open:
        pickle.dump(data, file_to_open)


def load_and_deserialize(filename):
    """
    load and deserialize data from the specified file
    """
    my_dict = {}
    with open(filename, "rb") as file_to_open:
        my_dict = pickle.load(file_to_open)
    return my_dict
