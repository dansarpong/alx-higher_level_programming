#!/usr/bin/python3
""" This module defines the Base class for the project """
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """

        if list_dictionaries is not None and list_dictionaries != []:
            return json.dumps(list_dictionaries)
        return "[]"
