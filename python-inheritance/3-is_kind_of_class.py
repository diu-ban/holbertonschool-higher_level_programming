#!/usr/bin/python3
"""
Module returns True if obj is an instance of a_class or a subclass; otherwise False.
"""

def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a subclass; otherwise False."""
    return isinstance(obj, a_class)
