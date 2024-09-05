#!/usr/bin/python3
import sys
if __name__ == "__main__":

    nb_arg = len(sys.argv)

    if nb_arg == 2:
        print("1 argument:")
    elif nb_arg == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(nb_arg - 1))

    for i in range(1, nb_arg):
        print("{}: {}".format(i, sys.argv[i]))
