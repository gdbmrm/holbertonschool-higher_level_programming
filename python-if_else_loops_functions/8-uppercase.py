#!/usr/bin/python3

def uppercase(str):
    for charactere in str:
        if 97 <= ord(charactere) <= 122:
            ord(charactere) == ord(charactere) - 32
        print(chr(ord(charactere)), end="")
