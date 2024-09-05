#!/usr/bin/python3

def uppercase(str):
    result = ""
    for charactere in str:
        if 97 <= ord(charactere) <= 122:
            result += chr(ord(charactere) - 32)
        else:
            result = result + charactere
    print(result)
