#!/usr/bin/python3
"""Function that add two integers"""


def add_integer(a, b=98):
    """sum two integers
    args:
        a: number
        b: number
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
