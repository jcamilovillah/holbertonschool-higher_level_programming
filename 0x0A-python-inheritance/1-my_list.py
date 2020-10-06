#!/usr/bin/python3
"""inherits from list."""


class MyList(list):
    """Class"""

    def print_sorted(self):
        """function"""
        list_c = []
        for i in sorted(self):
            list_c.append(i)
        print(list_c)
