#!/usr/bin/python3
"""
fonction qui affiche le contenu d'un fichier
"""


def read_file(filename=""):
    """
    fonction lecture de fichier
    """
    with open(filename, "r") as file_to_open:
        for line in file_to_open:
            print(line, end="")
