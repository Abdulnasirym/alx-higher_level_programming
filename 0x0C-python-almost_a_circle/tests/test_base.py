#!/usr/bin/python3
"""Defines unittests for base.py.

        Unittest classes:
            TestBase
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""
    def test_instancewith_id(self):
        """test when id is provided"""
        obj = Base(id=20)
        self.assertEqual(obj.id, 20)

    def test_instancewithout_id(self):
        """test when id is not provided"""
        obj1 = Base()
        obj2 = Base()

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)


if __name__ == "__main__":
    unittest.main()
