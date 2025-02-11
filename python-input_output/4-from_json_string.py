#!/usr/bin/python3

"""
Module: from_json_string

This module provides a function to deserialize a JSON string into a Python object.
"""

import json

def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The JSON string to be deserialized into a Python object.

    Returns:
        object: The Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
