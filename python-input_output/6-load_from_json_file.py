#!/usr/bin/python3
"""
Module: from_json_string

This module provides a function to deserialize a JSON string into a Python object.
"""

import json 

def load_from_json_file(filename):
    """
    Reads a JSON file and returns the deserialized content.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        object: The deserialized object from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    
