#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for i in my_string:
        if i in "cC":
            continue
        new_string = new_string + i
    return new_string
