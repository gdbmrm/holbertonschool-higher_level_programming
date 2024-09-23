#!/usr/bin/python3

def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    if type(obj) != a_class:
        if issubclass(type(obj), a_class):
            return True
    return False
