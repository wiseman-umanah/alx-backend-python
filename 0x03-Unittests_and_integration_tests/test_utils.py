#!/usr/bin/env python3
"""Familiarizing with utils.py"""
import unittest
from utils import access_nested_map, get_json
from parameterized import parameterized
from unittest.mock import patch, Mock


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


    class TestGetJson(unittest.TestCase):
        @patch('utils.requests.get')
        @parameterized.expand([
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False}),
        ])
        def test_get_json(self, test_url, test_payload, mock_get):
            """Test url with parameterize"""
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)
