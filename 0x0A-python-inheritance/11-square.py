#!/usr/bin/python3
"""Empty class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Instantiation"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """str"""
        return "[Square] " + str(self.__size) + "/" + str(self.__size)
