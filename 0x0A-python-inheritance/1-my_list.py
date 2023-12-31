#!/usr/bin/python3
"""a class that inherits from anotehr class"""


class MyList(list):
    def print_sorted(self):
        """function that prints list in sorted order"""
        print(sorted(self))
