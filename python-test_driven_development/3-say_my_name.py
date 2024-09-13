#!/usr/bin/python3
"""Definit une fonction qui affiche ton nom et ton nom de famille"""


def say_my_name(first_name, last_name=""):
    """Affiche un nom et un nom de famille
    first_name et last_name doivent etre des strings
    Raises:
        TypeError: if first_name or last_name isnt a string
    """

    if not isinstance(first_name, (str)):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, (str)):
        raise TypeError("last_name must be a string")

    string = "My name is {} {}"

    print(string.format(first_name, last_name))
