#!/usr/bin/python3
"""
fonction qui ecrit "text" dans "filename"
puis renvoie le nombre de charactere
"""


def write_file(filename="", text=""):
    """
    fonction write_file
    """
    count = 0
    with open(filename, "w+") as file_to_count:
        return file_to_count.write(text)
