#!/usr/bin/python3
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
        print("Added [{}] to the list.".format(item))
        super().append(item)

    def extend(self, x):
        """
        extend method
        """
        print("Extended the list with [{}] items.".format(len(x)))
        super().extend(x)


    def remove(self, item):
        """
        remove method
        """
        if item in self:
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
