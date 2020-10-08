#!/usr/bin/python3
"""returns the JSON representation of an object (string)"""
import json


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, "w", encoding="utf-8") as file:
        obj = json.dumps(my_obj)
        file.write(obj)
