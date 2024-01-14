#!/usr/bin/python3
""" This module defines the Base class for the project """


class Base:
    """ The Base class for the project """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The initializing function for the Base class """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
