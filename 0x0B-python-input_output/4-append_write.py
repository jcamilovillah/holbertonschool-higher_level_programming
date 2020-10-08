#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
