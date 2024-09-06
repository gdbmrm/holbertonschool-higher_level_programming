#!/usr/bin/python3

def uppercase(str):
    for charactere in str:
        if 97 <= ord(charactere) <= 122:
            charactere = chr(ord(charactere) - 32)
        print("{}".format(charactere), end="")
    print()
