#!/usr/bin/python3

def multiple_returns(sentence):

    length = 0
    for i in sentence:
        length += 1

    if length == 0:
        return(length, None)
    return(length, sentence[0])
