#!/usr/bin/python3
def multiple_returns(sentence):
    size = len(sentence)
    if size == 0:
        sentence[0] = ""
    return (size, sentence[0])
