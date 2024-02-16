#!/usr/bin/python3
# 6-from_json_string.py
"""Defines a JSON-to-string function."""
import Json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python object.

    Parameters:
        my_str (str): JSON string

    Returns:
        object: Python object represented by the JSON string
    """
    return json.loads(my_str)
