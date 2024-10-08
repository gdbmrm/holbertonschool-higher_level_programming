#!/usr/bin/python3

def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0
    elif roman_string is None:
        return 0
    elif len(roman_string) == 0:
        return 0

    resultat = 0
    my_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    for i in range(len(roman_string) - 1):
        if my_dict[roman_string[i]] < my_dict[roman_string[i + 1]]:
            resultat -= my_dict[roman_string[i]]
        else:
            resultat += my_dict[roman_string[i]]

    resultat += my_dict[roman_string[-1]]

    return resultat
