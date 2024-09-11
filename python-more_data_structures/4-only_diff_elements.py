#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    diff_elements = set_1.union(set_2)

    for element_1 in range(len(diff_elements) - 1):
        for element_2 in range(len(diff_elements)):
            if element_1 == element_2:
                diff_elements.remove(element_2)


    return(diff_elements)
    