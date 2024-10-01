#!/usr/bin/python3
"""
fonction qui renvoie la description du dictionnaire
avec une structure de données simple
(liste, dictionnaire, chaîne, nombre entier et booléen)
pour la sérialisation JSON d’un objet
"""


def class_to_json(obj):
    """
    fonction class to json
    """
    return obj.__dict__
