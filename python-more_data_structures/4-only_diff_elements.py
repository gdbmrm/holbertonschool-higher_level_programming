#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    diff_elements = []

    for element_1 in set_1:
        if element_1 not in set_2:
            diff_elements.append(element_1)

    for element_2 in set_2:
        if element_2 not in set_1:
            diff_elements.append(element_2)

    return diff_elements
