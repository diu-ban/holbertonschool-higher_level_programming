#!/usr/bin/python3
"""
Module: load_json
This module provides a function to load data from a JSON file.
"""

import json

def load_from_json_file(filename):
    """
    Load and return data from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        object: The Python object (dict, list, etc.) represented by the JSON data.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
        UnicodeDecodeError: If the file cannot be decoded using UTF-8.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f) 
