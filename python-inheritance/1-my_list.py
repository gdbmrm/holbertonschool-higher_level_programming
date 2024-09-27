#!/usr/bin/python3
"""
childclass of the class list
"""


class MyList(list):
    """
    childclass MyList
    """

    def print_sorted(self):
        """
        fonction qui affiche une liste croissante
        """
        print(sorted(self))
