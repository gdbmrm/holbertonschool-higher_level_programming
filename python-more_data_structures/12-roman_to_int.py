#!/usr/bin/python3

def roman_to_int(roman_string):

    resultat = 0
    my_dict = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 150,
        "M" : 1000
    }

    for chiffre_rom in roman_string:
        resultat += my_dict[chiffre_rom]

    return resultat
        