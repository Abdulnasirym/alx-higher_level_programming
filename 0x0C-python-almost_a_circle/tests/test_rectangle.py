#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
"""Testing the Rectangle class that inherits from base"""


class TestRectangle(unittest.TestCase):
    """testing the class"""
    def test_constructor_with_id(self):
        rectangle = Rectangle(id=1, width=5, height=3, x=2, y=1)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 1)

    def test_constructor_without_id(self):
        rectangle = Rectangle(width=5, height=3, x=2, y=1)
        self.assertEqual(rectangle.id, 2)

        rectangle2 = Rectangle(width=7, height=4, x=1, y=3)
        self.assertEqual(rectangle2.id, 3)

    def test_setters(self):
        rectangle = Rectangle(width=5, height=3, x=2, y=1)

        rectangle.width = 10
        self.assertEqual(rectangle.width, 10)

        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

        rectangle.x = 3
        self.assertEqual(rectangle.x, 3)

        rectangle.y = 5
        self.assertEqual(rectangle.y, 5)

        with self.assertRaises(TypeError) as context:
            rectangle.width = "invalid_width"
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.width = -5
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(TypeError) as context:
            rectangle.height = "invalid_height"
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

        with self.assertRaises(TypeError) as context:
            rectangle.x = "invalid_x"
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.x = -1
        self.assertEqual(str(context.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as context:
            rectangle.y = "invalid_y"
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.y = -2
        self.assertEqual(str(context.exception), "y must be >= 0")


if __name__ == '__main__':
    unittest.main()
