#!/usr/bin/python3
""" Module that returns the dictionary description of a data structure """


def class_to_json(obj):
    """ A function that returns the dictionary description
    of a data structure """

    ans = {}
    if hasattr(obj, "__dict__"):
        ans = obj.__dict__.copy()

    return ans
