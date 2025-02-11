#!/usr/bin/python3

"""
Module: to_json_string

This module provides a function to serialize a Python object into a JSON-formatted string.
"""
import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: The Python object to be serialized into a JSON string.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
