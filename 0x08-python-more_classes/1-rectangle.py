#!/usr/bin/python3
""" defines a Rectangle"""

class Rectangle:
    """Represent a rectangle"""
    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        self._width = value


    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        if self._height < 0:
            raise ValueError("height must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")

