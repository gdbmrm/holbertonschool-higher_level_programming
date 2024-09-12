#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    resultat = []
    i = 0

    for i in range(list_length + 1):
        try:
            if my_list_1[i] % my_list_2[i] == 0:
                resultat.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            resultat.append(0)
            print("division by 0")
        except TypeError:
            resultat.append(0)
            print("wrong type")
        except IndexError:
            resultat.append(0)
            print("out of range")

    return resultat
