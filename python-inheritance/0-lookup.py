#!/usr/bin/python3
"""
Module that provides a function to return the list of attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the attributes and methods of obj.
    """
    return dir(obj)
