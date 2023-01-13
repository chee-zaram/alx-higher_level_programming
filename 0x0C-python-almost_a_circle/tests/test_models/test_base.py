#!/usr/bin/python3
"""This is a test module"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestCase subclass"""

    def test_id(self):
        """Testing with expected inputs line `int` and `None`"""
        b1 = Base()
        b2 = Base(4)
        b3 = Base(-1)
        b4 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 4)
        self.assertEqual(b3.id, -1)
        self.assertEqual(b4.id, 0)
