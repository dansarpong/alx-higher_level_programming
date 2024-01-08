#!/usr/bin/python3
""" Defines a function to check an object's class """


def is_same_class(obj, a_class):
    """ Checks if an object is exactly an instance of a specified class """
    return (type(obj) == a_class)
