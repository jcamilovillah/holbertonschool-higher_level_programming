#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle class"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """init"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """define width"""
        return self.width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """define height"""
        return self.height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__height = value

    def area(self):
        """area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)
