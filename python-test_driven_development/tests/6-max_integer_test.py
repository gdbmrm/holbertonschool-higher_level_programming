#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_valid(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)

    def test_list_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_all_integers(self):
        self.assertIsInstance(max_integer([1, 2, 3]), int)


if __name__ == '__main__':
    unittest.main()
