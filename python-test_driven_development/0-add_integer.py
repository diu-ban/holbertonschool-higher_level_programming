#!/usr/bin/python3
"""
This module provides a function `add_integer` for adding two integers or floats.

It validates inputs and ensures proper type casting to integers.
"""
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns their sum.
    
    Args:
        a: First number, must be an integer or float.
        b: Second number, must be an integer or float (default is 98).
    
    Returns:
        The addition of a and b as an integer.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
