#!/usr/bin/python3

def uniq_add(my_list=[]):

    i = 0
    result = 0
    my_list = list(dict.fromkeys(my_list))

    for i in range(len(my_list)):
        result += my_list[i]

    return (result)
