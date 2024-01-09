#!/usr/bin/python3
""" Defines a function that writes a JSON representation to a text file """
import json


def save_to_json_file(my_obj, filename):
    """ A function that writes a JSON representation to a text file """

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
