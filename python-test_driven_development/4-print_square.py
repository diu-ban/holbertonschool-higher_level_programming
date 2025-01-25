#!/usr/bin/python3
"""
This module defines the function `print_square` which prints a square made 
of the character '#' based on the given size.
"""

def print_square(size):
    """
    Prints a square with the character '#' based on the provided size.
    
    Args:
        size (int): The size of the square.
    
    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        print('#' * size)
