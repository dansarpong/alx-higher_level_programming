#!/usr/bin/python3
def uppercase(str):
    upperstr = ""
    for c in str:
        if (ord('a') <= ord(c) <= ord('z')):
            upperstr = upperstr + (chr(ord('A') + (ord(c) - ord('a'))))
        else:
            upperstr = upperstr + c
    print("{:s}".format(upperstr))
