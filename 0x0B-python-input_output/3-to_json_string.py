#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation.

    Parameters:
        my_obj: Python object

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
