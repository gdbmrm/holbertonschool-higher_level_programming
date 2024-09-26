#!/usr/bin/python3
"""
fonction qui retourne la liste des attributs et méthodes d'une classe
"""


def lookup(obj):
    """
    retourne les attributs et méthodes de la class obj
    """
    return dir(obj)
