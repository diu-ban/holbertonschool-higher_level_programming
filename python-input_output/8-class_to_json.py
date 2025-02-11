#!/usr/bin/python3
"""
Module that converts a class instance to a JSON-serializable dictionary.
"""

def class_to_json(obj):
    """
    Returns the dictionary description of an object 
    for JSON serialization.

    Args:
        obj: An instance of a Class with serializable attributes 
             (list, dictionary, string, integer, and boolean).

    Returns:
        dict: A dictionary containing all the serializable attributes of the object.
    """
    return obj.__dict__
