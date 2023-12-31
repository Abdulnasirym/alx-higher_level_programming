#!/usr/bin/python3
"""checks if obj belongs to a_class"""


def is_kind_of_class(obj, a_class):
    """checks if the object belongs to an instance or
    child of an instance"""
    return isinstance(obj, a_class)
