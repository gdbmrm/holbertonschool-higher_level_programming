#!/usr/bin/python3
"""
function inherits_from
"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if type(obj) is not a_class:
        return isinstance(obj, a_class)
    return False
