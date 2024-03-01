#!/usr/bin/python3
"""
    Defines unittest for Rectangle
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Case for Rectangle"""
    def test_rectangle(self):
        """Test the creation of the Rectangle and the attributes values"""
        rectangle = Rectangle(width=10, height=12, x=3, y=4, id=5)

        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 4)
        self.assertEqual(rectangle.id, 5)

    def test_setters(self):
        """Test setters and getters"""
        rectangle = Rectangle(width=10, height=17, x=2, y=5)

        rectangle.width = 11
        rectangle.height = 12
        rectangle.x = 7
        rectangle.y = 6

        self.assertEqual(rectangle.width, 11)
        self.assertEqual(rectangle.height, 12)
        self.assertEqual(rectangle.x, 7)
        self.assertEqual(rectangle.y, 6)

    def test_invalid_inputs(self):
        """Test invalid values entered into the function"""
        rectangle = Rectangle(width=15, height=11, x=9, y=7, id=1)

        rectangle.width = -5
        rectangle.height = 0
        self.assertEqual(rectangle.width, 15)
        self.assertEqual(retangle.height, 11)

    def test_width(self):
        """Test for invalid width"""
        rectangle = Rectangle(width=10, height=5, x=2, y=3)

        with self.assertRaises(TypeError) as context:
            rectangle.width = "invalid_width"
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.width = -5
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_height(self):
        """Test for invalid width"""
        rectangle = Rectangle(width=10, height=5, x=2, y=3)

        with self.assertRaises(TypeError) as context:
            rectangle.height = "invalid_height"
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")


if __name__ == "__main__":
    unittest.main()
