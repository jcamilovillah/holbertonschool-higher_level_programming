#!/usr/bin/python3
"""print text with \n"""


def text_indentation(text):
    """function that print a text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    for j in text:
        if j == "." or j == "?" or j == ":":
            print(j)
            print()
        else:
            print(j, end="")
