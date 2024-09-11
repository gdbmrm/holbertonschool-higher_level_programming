#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    real_number = 0
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            real_number += 1
        print()
        return real_number
    except (IndexError, TypeError):
        print()
        return real_number
