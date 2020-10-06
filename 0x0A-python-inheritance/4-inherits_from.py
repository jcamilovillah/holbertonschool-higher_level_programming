#!/usr/bin/python3
"""he object is an instance of a class that inherited
 (directly or indirectly) from the specified class"""


def inherits_from(obj, a_class):
    """Function"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
