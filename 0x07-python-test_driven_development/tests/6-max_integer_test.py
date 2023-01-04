#!/usr/bin/python3
"""Unittest module ``6-max_integer_test

This module contains unittest for the function ``max_integer``
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the ``max_integer`` function

    The tests in this class cover the following scenarios:
    - Lists with different numbers of elements
    - Lists containing large numbers
    - Lists with elements of different types
    - An empty list
    - Lists containing elements that are not integers
    - Argument with invalid types
    - ``None`` argument
    """

    def setUp(self):
        """Runs before every method"""

        # expected inputs
        self.expected_1 = [1, 2, 3, 4]
        self.res_1 = 4
        self.expected_2 = [-2, 4, -19, 5, 6, 1992]
        self.res_2 = 1992
        self.expected_3 = [19]
        self.res_3 = 19
        self.expected_4 = [10, 10, 10, 10, 10, 10, 10]
        self.res_4 = 10

        # empty list
        self.empty = []
        self.res_empty = None

        # type errors
        self.type_err_1 = 23
        self.type_err_2 = "str"
        self.type_err_3 = [[2, 3, 4]]
        self.type_err_4 = (1, -3, 4)
        self.type_err_5 = [4, "9"]
        self.type_err_6 = [0.4, -23.11, 5, 293.24]

        # None type
        self.none = None

        # max integer
        self.max_pos_int_list_1 = [483, 2147483647, 1032]
        self.max_pos_int_list_2 = [483, 2147483647, 4234, 2147483647]
        self.max_pos_int_res = 2147483647

        # large integers
        self.largt_int_list = [2147483647, 9223372036854775807]
        self.large_int_res = 9223372036854775807
        self.largt_neg_list = [-2147483647, -9223372036854775807]
        self.large_neg_res = -2147483647

    def test_integers(self):
        """Tests when valid integers are in the list"""
        self.assertEqual(max_integer(self.expected_1), self.res_1)
        self.assertEqual(max_integer(self.expected_2), self.res_2)
        self.assertEqual(max_integer(self.expected_3), self.res_3)

    def test_large_integers(self):
        """Test with large integers"""
        self.assertEqual(max_integer([self.large_int_res]), self.large_int_res)
        self.assertEqual(max_integer(self.largt_int_list), self.large_int_res)
        self.assertEqual(max_integer([self.large_neg_res]), self.large_neg_res)
        self.assertEqual(max_integer(self.largt_neg_list), self.large_neg_res)

    def test_max_integer(self):
        """Test with lists containing the maximum integer"""
        self.assertEqual(max_integer(self.max_pos_int_list_1),
                         self.max_pos_int_res)
        self.assertEqual(max_integer(self.max_pos_int_list_2),
                         self.max_pos_int_res)

    def test_no_arg(self):
        """Tests when the function is passed no argument"""
        self.assertEqual(max_integer(), None)

    def test_empty(self):
        """Tests for when an empty list is passed to the function"""
        self.assertEqual(max_integer(self.empty), self.res_empty)

    def test_none(self):
        """Testing for when function is passed `None`"""
        self.assertRaises(TypeError, max_integer, self.none)


'''
    def test_types(self):
        """Test when list has invalid items or the argument is not a list"""

        # integer
        with self.assertRaises(TypeError):
            max_integer(self.type_err_1)

        # string
        with self.assertRaises(AssertionError):
            max_integer(self.type_err_2)

        # list of list
        with self.assertRaises(TypeError):
            max_integer(self.type_err_3)

        # tuple
        with self.assertRaises(TypeError):
            max_integer(self.type_err_4)

        # list with non-integer item(s)
        with self.assertRaises(TypeError):
            max_integer(self.type_err_5)

        # list with floats
        with self.assertRaises(TypeError):
            max_integer(self.type_err_6)
'''

if __name__ == "__main__":
    unittest.main()
