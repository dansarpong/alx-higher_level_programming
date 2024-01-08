#!/usr/bin/python3
""" Defines a Square class that inherits from Rectangle """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ A square class based on Rectangle """

    def __init__(self, size):
        """ Initializes a Square instance """

        self.integer_validator("size", size)

        self.__size = size
        super().__init__(size, size)
