#!/usr/bin/python3
def magic_string():
    setattr(magic_string, "n", getattr(magic_string, "n", -1) + 1)
    return "Holberton" + ", Holberton" * magic_string.n
