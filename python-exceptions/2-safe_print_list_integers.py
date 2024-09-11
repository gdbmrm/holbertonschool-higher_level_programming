#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):

    real_number = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            real_number += 1
        except (IndexError, TypeError):
            continue

    print()
    return real_number
