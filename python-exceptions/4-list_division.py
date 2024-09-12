#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    resultat = []
    i = 0

    for i in range(list_length + 1):
        try:
            if my_list_1[i] % my_list_2[i] == 0:
                resultat.append(my_list_1[i] % my_list_2[i])
            else:
                resultat.append(0)
        except Exception as e:
            print(e)
    
    return resultat
