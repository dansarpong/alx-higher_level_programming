#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    new_list = my_list[:]
    new_list.reverse()
    for i in new_list:
        print("{}".format(i))
