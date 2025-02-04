#!/usr/bin/python3
"""
Module define BaseGeometry class.
"""

class BaseGeometry:
    """A class representing geometry with an unimplemented area method."""

    def area(self):
        """Raises an exception because the method is not implemented."""
        raise Exception("area() is not implemented") 
    