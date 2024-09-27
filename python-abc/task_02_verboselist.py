#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
class verboselist
"""


class VerboseList(list):
    """
    childclass of list class
    """
    def append(self, item):
        """
        append method
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, x):
        """
        extend method
        """
        super().extend(x)
        print("Extended the list with [{}] items.".format(len(x)))

    def remove(self, item):
        """
        remove method
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, x=None):
        """
        pop method
        """
        if x is None:
            x = -1
        print("Popped [{}] from the list.".format(self[x]))
        super().pop(x)
