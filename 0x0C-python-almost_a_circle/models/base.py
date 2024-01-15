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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """

        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string """

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all atributes already set """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new
