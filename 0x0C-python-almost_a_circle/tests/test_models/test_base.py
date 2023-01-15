#!/usr/bin/python3
"""This is a test module for the `Base` class in the ``models`` package"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """TestCase subclass"""

    def setUp(self):
        """Method to run at the start of each test method"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Check if `id` atttribute is accurate"""

        b1 = Base()
        b2 = Base(4)
        b3 = Base(-1)
        sq1 = Square(2)
        b4 = Base(0)
        rect1 = Rectangle(1, 2)
        b5 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, -1)
        self.assertEqual(sq1.id, 2)
        self.assertEqual(b4.id, 0)
        self.assertEqual(rect1.id, 3)
        self.assertEqual(b5.id, 4)
        b5.id = 5
        self.assertEqual(b5.id, 5)

    def test_inheritance(self):
        """Test `Square` and `Rectangle` inheritance from `Base`"""

        base1 = Base()
        rect1 = Rectangle(1, 2)
        rect2 = Rectangle(1, 2)

        self.assertTrue(type(base1) == Base)
        self.assertTrue(isinstance(base1, Base))

        self.assertTrue(type(rect1) == Rectangle)
        self.assertTrue(isinstance(rect1, Rectangle))
        self.assertFalse(rect1 is Rectangle)

        self.assertTrue(isinstance(rect1, Base))
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertFalse(issubclass(Base, Rectangle))
        self.assertFalse(str(rect1) == str(base1))

        self.assertFalse(str(rect1) == str(rect2))
        self.assertFalse(rect1 is rect2)
        self.assertFalse(base1 is rect1)

        sq1 = Square(1)
        sq2 = Square(1)

        self.assertTrue(type(base1) == Base)
        self.assertTrue(isinstance(base1, Base))

        self.assertTrue(type(sq1) == Square)
        self.assertTrue(isinstance(sq1, Square))
        self.assertTrue(isinstance(sq1, Rectangle))
        self.assertFalse(sq1 is Square)

        self.assertTrue(isinstance(sq1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(issubclass(Base, Square))
        self.assertFalse(issubclass(Rectangle, Square))
        self.assertFalse(str(sq1) == str(base1))

        self.assertFalse(str(sq1) == str(sq2))
        self.assertFalse(sq1 is sq2)
        self.assertFalse(base1 is sq1)

        self.assertFalse(sq1 is rect1)

    def test_create(self):
        """Test the `create` class method with expected input"""
        pass


if __name__ == "__main__":
    unittest.main()
