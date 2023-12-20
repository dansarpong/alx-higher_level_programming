#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """ A Square class with private and optional instantion attribute: size """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes the square """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ get the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """ set the position of the square """
        if type(value) is tuple and len(value) is 2 and \
            type(value[0]) is int and type(value[1]) is int and \
                value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ Finds and returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints a square of __size with # at position """
        if self.__size > 0:
            for y in range(self.__position[1]):
                print()
            for x in range(self.__size):
                print(' ' * self.__position[0], end='')
                print('#' * self.__size)
        else:
            print()
