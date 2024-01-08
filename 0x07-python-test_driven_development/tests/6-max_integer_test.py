#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unitest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docstring"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        self.assertIsNone(max_integer([]))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_arg(self):
        """Tests for one argument passed to func"""
        self.assertEqual(max_integer([1]), 1)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        self.assertEqual(max_integer([200, 10, 8, 36, 14, 50]), 200)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        self.assertEqual(max_integer([2, 10, 8, 36, 14, 50]), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        self.assertEqual(max_integer([2, 10, 8, 360, 14, 50]), 360)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        self.assertEqual(max_integer([200, 10, 8, -36, 14, 50]), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        self.assertEqual(max_integer([-6, -50, -75, -1, -100]), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string(self):
        """Test a string with characters."""
        string = "string"
        self.assertEqual(max_integer(string), 't')

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)


if __name__ == '__main__':
    unittest.main()
