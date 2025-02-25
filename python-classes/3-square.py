#!/usr/bin/python3
"""
This module defines a Square class.

The Square class represents a square with a private size attribute and 
includes a method to compute its area.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
