#!/usr/bin/python3

"""
Module: add_items_to_json

This module adds all command-line arguments to a list,
and saves the list to a JSON file named 'add_item.json'.
It loads the existing content of 'add_item.json' (if any),
appends new command-line arguments to it, and then saves the updated list.
"""

import sys
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
    
def main():
    """
    Adds command-line arguments to a list and saves it to a JSON file.

    This function loads an existing list from 'add_item.json' (if the file exists),
    appends all new command-line arguments to it, and saves the updated list 
    back to the file in JSON format. If the file does not exist, it initializes 
    an empty list, appends the arguments, and creates the file.
    
    The list is saved as a JSON representation in 'add_item.json'.
    """
    filename = "add_item.json"
    try: 
        items = load_from_json_file(filename)
    except (FileNotFoundError, ValueError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
