#!/usr/bin/python3
""" Définit une fonction qui affiche un texte 
avec des retours a la ligne après des . ? et :"""


def text_indentation(text):
    """Affiche un texte avec des retours a la ligne après des . ? et :
    Raises:
        TypeError: if text isnt a string
    """


    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i, end="")
            print()
            print()
        else:
            print(i, end="")
