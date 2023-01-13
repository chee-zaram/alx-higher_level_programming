#!/usr/bin/python3
"""Tests for the ``Rectangle`` class in the ``rectangle`` module

The ``rectangle`` module is i the ``models`` package"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the ``Rectangle`` class"""

    def test_inheritance(self):
        """Testing if the class properly inherits from its base class"""
        r1 = Rectangle(2, 4)
        self.assertEqual(r1.id, 1)
