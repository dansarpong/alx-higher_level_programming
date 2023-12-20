#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ A Square class with private and optional instantion attribute: size """
    def __init__(self, size=0):
        """ initializes the square """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
