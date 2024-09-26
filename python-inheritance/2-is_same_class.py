#!/usr/bin/python3
"""
fonction is_same_class
"""


def is_same_class(obj, a_class):
    """
    fonction qui check si obj est une instance
    de a_class
    """
    return type(obj) is a_class
