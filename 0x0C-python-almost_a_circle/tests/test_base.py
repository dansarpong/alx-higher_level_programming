#!/usr/bin/python3
""" This module defines a test for the base model """
import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """ Defines the TestBase class to test the base model """

    def test_base_init(self):
        """ Function to test the base init funtion """
        base1 = Base()
        self.assertEqual(base1.id, 1, "id should be the same as 1")

        id = 15
        base2 = Base(id)
        self.assertEqual(base1.id, id, f"id should be the same as {id}")
        
        base3 = Base()
        self.assertEqual(base1.id, 2, "id should be the same as 2")

    def test_base_nb_objects(self):
        """ Function to test the private class attribute __nb_objects"""

        base1 = Base()
        base2 = Base()
        base3 = Base()
        base4 = Base()
        self.assertEqual(base4.id, 4, "id should be the same as 4")

    def test_base_id(self):
        """ Function to test the id passed """

        id = 21
        base2 = Base(id)
        self.assertEqual(base2.id, id, f"id should be the same as {id}")

        id = "fan"
        base3 = Base(id)
        self.assertEqual(base3.id, id, "id is ALWAYS assumed to be integer")


if __name__ == "__main__":
    unittest.main()