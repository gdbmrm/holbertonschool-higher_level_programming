#!/usr/bin/python3
"""
childclass of the class list
"""


class MyList(list):
    def __init__(self):
        """
        constructeur de la classe
        """
        super().__init__()

    def print_sorted(self):
        """
        fonction qui affiche une liste croissante
        """
        print(sorted(self))
