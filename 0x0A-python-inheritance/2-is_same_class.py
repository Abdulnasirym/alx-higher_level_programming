#!/usr/bin/python3
"""checks if an object is am instance of a class"""


def is_same_class(obj, a_class):
    """The function"""
    if type(obj) == a_class:
        return True
    else:
        return False
