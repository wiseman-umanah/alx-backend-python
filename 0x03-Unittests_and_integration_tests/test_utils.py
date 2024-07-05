#!/usr/bin/env python3
"""Familiarizing with utils.py"""
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Class to test across units    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, res):
        """test access map

        Args:
            nested_map (dict): the dict to map
            path (tuple): value to search
            res (str | Dict): the result
        """
        self.assertEqual(access_nested_map(nested_map, path), res)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test for KeyError"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
