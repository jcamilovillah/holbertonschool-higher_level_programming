#!/usr/bin/python3
"""return n characters"""


def write_file(filename="", text=""):
    """function"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
