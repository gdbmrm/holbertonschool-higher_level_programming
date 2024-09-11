#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    mapped_numbers = list(map(lambda x: x * number, my_list))
    return(mapped_numbers)
