#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test a list with multiple elements"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_elements(self):
        """Test a list with negative and positive elements"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_all_equal(self):
        """Test a list where all elements are the same"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test a list with float elements"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)

    def test_mixed_types(self):
        """Test a list with mixed types (integers and floats)"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)

    def test_none_in_list(self):
        """Test a list containing None, should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([None, 1, 2, 3])

    def test_string_in_list(self):
        """Test a list containing a string, should raise TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "string", 3])

if __name__ == '__main__':
    unittest.main()
