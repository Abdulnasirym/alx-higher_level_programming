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

    def test_validation(self):
        # Test valid instantiation
        rectangle = Rectangle(width=5, height=3, x=2, y=3, id=1)

        # Test invalid width
        with self.assertRaises(TypeError) as context:
            rectangle.width = "invalid_width"
        self.assertEqual(str(context.exception), "width must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.width = -5
        self.assertEqual(str(context.exception), "width must be > 0")

        # Test invalid height
        with self.assertRaises(TypeError) as context:
            rectangle.height = "invalid_height"
        self.assertEqual(str(context.exception), "height must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.height = 0
        self.assertEqual(str(context.exception), "height must be > 0")

        # Test invalid x
        with self.assertRaises(TypeError) as context:
            rectangle.x = "invalid_x"
        self.assertEqual(str(context.exception), "x must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.x = -1
        self.assertEqual(str(context.exception), "x must be >= 0")

        # Test invalid y
        with self.assertRaises(TypeError) as context:
            rectangle.y = "invalid_y"
        self.assertEqual(str(context.exception), "y must be an integer")

        with self.assertRaises(ValueError) as context:
            rectangle.y = -2
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_area(self):
        rectangle = Rectangle(width=5, height=3)
        self.assertEqual(rectangle.area(), 15)

if __name__ == '__main__':
    unittest.main()
