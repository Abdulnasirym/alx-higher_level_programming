#!/usr/bin/python3
"""checks if the object is an instance of a class"""


def inherits_from(obj, a_class):
    """returns True if obj is an instance of a class
    inherited directly or indirectly and False otherwise
    """
    return type(obj) != a_class and isinstance(obj, a_class)
