#!/usr/bin/python3

for i in range(0, 9):
    for j in range(0, 10):
        if i != j and j > i:
            if i == 8 and j == 9:
                print("{}{}".format(i, j))
            else:
                print("{}{}, ".format(i, j), end="")
