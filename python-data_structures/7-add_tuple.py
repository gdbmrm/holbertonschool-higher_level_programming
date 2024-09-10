#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if len(list_a) >= 3:
        list_a = list_a[:2]
    else:
        if len(list_a) == 0:
            list_a.append(0)
            list_a.append(0)
        if len(list_a) == 1:
            list_a.append(0)

    if len(list_b) >= 3:
        list_b = list_b[:2]
    else:
        if len(list_b) == 0:
            list_b.append(0)
            list_b.append(0)
        if len(list_b) == 1:
            list_b.append(0)

    result_1 = list_a[0] + list_b[0]
    result_2 = list_a[1] + list_b[1]

    return(result_1, result_2)
