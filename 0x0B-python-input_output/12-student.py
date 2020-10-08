#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """Class"""

    def __init__(self, first_name, last_name, age):
        """Init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict"""
        lis = {}
        if attrs is None:
            return self.__dict__

        for i, j in self.__dict__.items():
            if i in attrs:
                    lis[i] = j
        return lis
