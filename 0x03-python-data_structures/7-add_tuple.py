#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_list = []
    for i in range(2):
        a = tuple_a[i] if i < len_a else 0
        b = tuple_b[i] if i < len_b else 0
        new_list.append(a + b)
    return tuple(new_list)
