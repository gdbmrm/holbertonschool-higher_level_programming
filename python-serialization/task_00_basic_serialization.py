#!/usr/bin/env python3
"""
module basic serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serialize and save data to the specified file
    """
    with open(filename, "w") as file_to_open:
        json.dump(data, file_to_open)


def load_and_deserialize(filename):
    """
    load and deserialize data from the specified file
    """
    with open(filename, "r") as file_to_open:
        return json.load(file_to_open)
