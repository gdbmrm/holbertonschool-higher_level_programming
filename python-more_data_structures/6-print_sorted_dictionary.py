#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    item = sorted(a_dictionary.items())

    for key, values in item:
        print("{}: {}".format(key, values))
