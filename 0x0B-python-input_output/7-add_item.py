#!/usr/bin/python3
""" A script that adds arguments to a Python list then save them to a file """
import os.path
import sys
import json

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


filename = "add_item.json"

if os.path.isfile(filename):
    my_obj = load_from_json_file(filename)
else:
    my_obj = []

my_obj.extend(sys.argv[1:])

save_to_json_file(my_obj, filename)
