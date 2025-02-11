#!/usr/bin/python3
"""
Module: save_to_json
This module provides a function to load data from a JSON file.
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to serialize into JSON.
        filename (str): The name of the file to save the JSON data.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
