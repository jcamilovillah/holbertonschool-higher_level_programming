#!/usr/bin/python3
"""Base"""
import json


class Base():
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json to file"""
        lis = []
        for i in list_objs:
            lis.append(i.to_dictionary())
        json = cls.to_json_string(lis)
        with open(cls.__name__ + ".json", "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                file.write(json)

    @staticmethod
    def from_json_string(json_string):
        """list json"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return instance"""
        if cls.__name__ == "Rectangle":
            obj = cls(4, 5, 5, 4)
            obj.update(**dictionary)
            return obj
        else:
            obj = cls(4, 5, 5, 4)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """list of instances"""
        lis = []
        try:
            with open(cls.__name__ + ".json", "r") as file:
                cont = file.read()
            des = cls.from_json_string(cont)
            for i in des:
                lis += [cls.create(**i)]
            return lis
        except:
            return []
