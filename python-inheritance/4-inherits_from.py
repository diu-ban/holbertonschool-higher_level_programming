#!/usr/bin/python3
"""
Module returns True if obj is an instance of a subclass of a_class (but not a_class itself).
"""

def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a subclass of a_class (but not a_class itself)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
