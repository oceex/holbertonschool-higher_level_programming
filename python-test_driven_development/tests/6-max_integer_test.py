#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        unittest.assertEqual(max_integer([]), None)
        unittest.assertEqual(max_integer([1, 3, 5, 1]), 5)
        unittest.assertEqual(max_integer([-1, -9, -2, 0]), 0)
        unittest.assertEqual(max_integer([2, -5, 3, 0, -7]), 3)
