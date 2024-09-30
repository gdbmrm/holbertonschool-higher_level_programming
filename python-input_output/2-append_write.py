#!/usr/bin/python3
"""
fonction qui ajoute du text ("text") dans le fichier "filename"
"""


def append_write(filename="", text=""):
    """
    fonction append_write
    """
    with open(filename, "a+") as file_to_open:
        return file_to_open.write(text)
