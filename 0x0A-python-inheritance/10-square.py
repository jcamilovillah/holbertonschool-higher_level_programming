#!/usr/bin/python3
"""Empty class"""


class BaseGeometry:
    """Class"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Instantiation"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """area"""
        return self.__width * self.__height

    def print(self):
        """print"""
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)


class Square(Rectangle):
    """Square"""

    def __init__(self, size):
        """Instantiation"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)
        
    def area(self):
        return self.__size * self.__size
