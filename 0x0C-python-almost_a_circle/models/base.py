#!/usr/bin/python3
"""
    Creating the base class for all classes
"""


class Base:
    """Base model

    This This is the base of all classes in the "python almost a circle project

    private Clss Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """initiate a new base.

        Args:
            id(int): The id of the new base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
