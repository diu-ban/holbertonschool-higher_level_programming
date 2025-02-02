#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square shape with a private size attribute.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
