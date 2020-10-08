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
        if attrs:
            for i, j in self.__dict__.items():
                for x in attrs:
                    if i == x:
                        lis[i] = j
            return lis
        return self.__dict__
