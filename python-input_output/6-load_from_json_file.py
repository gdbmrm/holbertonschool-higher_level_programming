#!/usr/bin/python3
"""
fonction qui ouvre un fichier puis
convertit les chaines json du fichier en objet python
"""
import json


def load_from_json_file(filename):
    """
    fonction load from json file
    """
    with open(filename, "r") as file_to_convert:
        for line in file_to_convert:
            objet = json.loads(line)
    return objet
