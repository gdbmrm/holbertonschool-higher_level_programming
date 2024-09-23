#!/usr/bin/python3
"""
childclass of the class list
"""


class MyList(list):
    def __init__(self):
        """
        constructeur
        """
        super().__init__()

    def print_sorted(self):
        """
        fonction qui affiche une liste croissante
        """
        liste = sorted(self)

        print("[", end="")
        for i in range(len(liste) - 1):
            print("{}, ".format(liste[i]), end="")
        print("{}]".format(liste[i + 1]))
