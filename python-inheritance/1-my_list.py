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
        liste = sorted(self)
        print(liste)

if __name__ == "__main__":
    my_list = MyList([1, 5, 9, 6, 8])
    my_list.print_sorted() 