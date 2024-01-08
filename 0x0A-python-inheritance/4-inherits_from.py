#!/usr/bin/python3
""" Defines a function to check an object's class """


def inherits_from(obj, a_class):
    """ Checks if an object is an inherited instance of a specified class """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
