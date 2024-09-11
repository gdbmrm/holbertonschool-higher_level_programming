#!/usr/bin/python3

def best_score(a_dictionary):

    max = 0
    max_key = ""

    if bool(a_dictionary) is False:
        return None

    for key, item in a_dictionary.items():
        if item > max:
            max = item
            max_key = key

    return max_key
