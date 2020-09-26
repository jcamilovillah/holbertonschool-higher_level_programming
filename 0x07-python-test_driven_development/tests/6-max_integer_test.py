#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Create"""


def test_area(self):
    """test"""
    self.assertAlmostEqual(max_integer[3, 12, 2, 2], 12)
    self.assertAlmostEqual(max_integer[3, -12, 2, 2], 3)
    self.assertAlmostEqual(max_integer[-3, -12, -2, -1], -2)
    self.assertAlmostEqual(max_integer[-3, -12, -2, -2], -2)
    self.assertAlmostEqual(max_integer([]), None)
    self.assertAlmostEqual(max_integer[1], 1)
    self.assertAlmostEqual(max_integer, None)
    self.assertAlmostEqual(max_integer(), None)
    self.assertNotEqual(max_integer([3, 2, 5]), 8)
    self.assertNotIn(max_integer([5, 4, 6]), [9, 4, 2])
    self.assertIsInstance(max_integer([5, 4, 6]), int)
    self.assertTrue(max_integer([5, 4, 6]), int)
    self.assertFalse(max_integer([0, 0, 0]), False)

if __name__ == '__main__':
    unittest.main()
