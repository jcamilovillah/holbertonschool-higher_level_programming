#!/usr/bin/python3
"""print number lines"""


def number_of_lines(filename=""):
    """function"""
    with open(filename, encoding="utf-8") as file:
        return len(file.readlines())
