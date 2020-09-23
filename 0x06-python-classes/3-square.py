#!/usr/bin/python3
"""Class that define as the point zero"""


class Square:
    """Class square"""
    __size = 0

    def __init__(self, size=0):
        """Private size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
