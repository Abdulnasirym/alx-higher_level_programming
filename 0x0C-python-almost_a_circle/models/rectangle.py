#!/usr/bin/python3
"""
    Creating a Reactangle class that inherits from Base
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle model"""
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_positive_integer(value, 'width')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_positive_integer(value, 'height')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_non_negative_integer(value, 'x')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_non_negative_integer(value, 'y')
        self.__y = value

    def validate_positive_integer(self, value, attribute_name):
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value <= 0:
            raise ValueError(f"{attribute_name} must be > 0")

    def validate_non_negative_integer(self, value, attribute_name):
        if not isinstance(value, int):
            raise TypeError(f"{attribute_name} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute_name} must be >= 0")

    def area(self):
        return self.__width * self.__height
