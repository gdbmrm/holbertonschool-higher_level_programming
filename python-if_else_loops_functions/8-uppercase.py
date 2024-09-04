#!/usr/bin/python3

def uppercase(str):
    for charactere in str:
        if 97 <= ord(charactere) <= 122:
            print(chr(ord(charactere) - 32), end="" )
        else:
            print(charactere, end="")
    print()
