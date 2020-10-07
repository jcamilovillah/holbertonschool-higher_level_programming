#!/usr/bin/python3
"""read lines"""


def read_lines(filename="", nb_lines=0):
    """function"""
    nlines = len(open(filename).readlines())
    with open(filename, encoding="utf-8") as file:
        if nb_lines > 0 and nb_lines < nlines:
            for lines in range(nb_lines):
                print(file.readline(), end="")
        else:
            print(file.read(), end="")
