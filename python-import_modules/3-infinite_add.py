#!/usr/bin/python3
import sys
from add_0 import add
if __name__ == "__main__":

    nb_arg = len(sys.argv)
    result = 0

    for i in range(1, nb_arg):
        result += int(sys.argv[i])

    print(result)
