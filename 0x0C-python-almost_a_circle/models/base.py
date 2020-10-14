#!/usr/bin/python3
"""create a class"""


class Base():
    """create a class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init of class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects