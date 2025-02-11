#!/usr/bin/python3

"""
Module: add_items_to_json

This module adds all command-line arguments to a list,
and saves the list to a JSON file named 'add_item.json'.
It loads the existing content of 'add_item.json' (if any),
appends new command-line arguments to it, and then saves the updated list.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

def main():
    """
    Adds command-line arguments to a list and saves it to a JSON file.

    This function loads an existing list from 'add_item.json' (if the file exists),
    appends all new command-line arguments to it, and saves the updated list 
    back to the file in JSON format. If the file does not exist, it initializes 
    an empty list, appends the arguments, and creates the file.
    
    The list is saved as a JSON representation in 'add_item.json'.
    """
    try: 
        items = load_from_json_file(filename)
    except (FileNotFoundError, ValueError):
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
