#!/usr/bin/python3
"""Function that print My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """print My name is <first name> <last name>
    args:
        first_name: original
        last_name: number for div
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
