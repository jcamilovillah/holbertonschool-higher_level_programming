#!/usr/bin/python3
"""class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """create a class called rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """method init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """method getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """method getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """method setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method area"""
        return self.__height * self.__width

    def display(self):
        """method display"""
        space = ""
        for y in range(self.__y):
            print()
        for x in range(self.__x):
            space += " "
        for i in range(self.__height):
            print(space, end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """method str"""
        return "[Rectangle] " + "(" + str(self.id) + ") "\
            + str(self.__x) + "/" + str(self.__y) + " - " +\
            str(self.__width) + "/" + str(self.__height)

    def update(self, *args, **kwargs):
        """method update"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.__width = args[i]
                if i == 2:
                    self.__height = args[i]
                if i == 3:
                    self.__x = args[i]
                if i == 4:
                    self.__y = args[i]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.__width = value
            if key == "height":
                self.__height = value
            if key == "x":
                self.__x = value
            if key == "y":
                self.__y = value

    def to_dictionary(self):
        """method dictionary"""
        return dict(id=self.id, width=self.width,
                    height=self.height, x=self.x, y=self.y)
