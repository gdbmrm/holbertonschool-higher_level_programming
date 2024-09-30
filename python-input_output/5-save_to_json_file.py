#!/usr/bin/python3
import json
"""
 fonction qui écrit un objet dans un fichier texte,
en utilisant une représentation JSON
 """


def save_to_json_file(my_obj, filename):
    """
    fonction save_to_json_file
    """
    with open(filename, "a+") as file_to_open:
        file_to_open.write(json.dumps(my_obj))
