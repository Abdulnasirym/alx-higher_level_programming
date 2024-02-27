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

    def test_area(self):
        """Testing the area of the rectangle"""
        rectangle = Rectangle(width=3, height=4, x=2, y=5, id=2)
        self.assertEqual(rectangle.area(), 12)


if __name__ == "__main__":
    unittest.main()
