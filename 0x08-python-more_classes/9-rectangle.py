#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                val += str(self.print_symbol) * self.__width
                val += '\n'
        return val[:-1]

    def __repr__(self):
        """print2"""
        return 'Rectangle(%d, %d)' % (self.__width, self.__height)

    def __del__(self):
        """del method"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ More bigger than"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """new Rectangle instance with width == height == size"""
        return cls(size, size)
