#!/usr/bin/python3
"""
Module define BaseGeometry class.
"""

class BaseGeometry:
    """A class representing geometry with an unimplemented area method."""

    def area(self):
        """Raises an exception because the method is not implemented."""
        raise Exception("area() is not implemented") 
    
    def integer_validator(self, name, value):
        """ Validates values

        Args:
            name (string): A string.
            value (int): A number.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        