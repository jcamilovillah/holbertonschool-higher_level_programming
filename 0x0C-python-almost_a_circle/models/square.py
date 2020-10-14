#!/usr/bin/python3
"""Class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] " + "(" + str(self.id) + ") "\
            + str(self.x) + "/" +\
            str(self.y) + " - " + str(self.width)

    @property
    def size(self):
        """method getter"""
        return self.width

    @size.setter
    def size(self, size):
        """method setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """method update"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "size":
                self.size = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        """method dictionary"""
        return dict(id=self.id, size=self.size, x=self.x, y=self.y)
