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
        data_json = pickle.dump(data)
        file_to_open.write(data_json)


def load_and_deserialize(filename):
    """
    load and deserialize data from the specified file
    """
    with open(filename, "rb") as file_to_open:
        return pickle.load(file_to_open)
