#!/usr/bin/python3

"""
Module: load_json

Module that adds all command-line arguments to a list,
and saves them to a JSON file (add_item.json).
"""

import sys
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try: 
    items = load_from_json_file(filename)
except (FileNotFoundError, ValueError):
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
