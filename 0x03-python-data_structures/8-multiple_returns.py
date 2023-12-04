#!/usr/bin/python3
def multiple_returns(sentence):
    len_s = len(sentence)
    if len_s == 0:
        first = None
    else:
        first = sentence[0]
    return tuple([len_s, first])
