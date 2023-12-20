#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ A Square class with private and optional instantion attribute: size """
    def __init__(self, size=0):
        """ initializes the square """
        self.size = size

    @property
    def size(self):
        """ gets the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size attribute """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Finds and returns the current square area """
        return self.__size ** 2
