#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """print"""
        val = ""
        if self.__width > 0 and self.__height > 0:
            for i in range(self.__height):
                val += "#" * self.__width
                val += '\n'
        return val[:-1]

    def __repr__(self):
        """print2"""
        return 'Rectangle(%d, %d)' % (self.__width, self.__height)

    def __del__(self):
        """del method"""
        print("Bye rectangle...")
