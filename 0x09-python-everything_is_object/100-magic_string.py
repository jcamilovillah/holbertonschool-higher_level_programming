#!/usr/bin/python3
def magic_string():
    count = 0
    if hasattr(magic_string, 'n'):
        count = getattr(magic_string, "n")
    setattr(magic_string, "n", count)
    return "Holberton" * magic_string.n
