#!/usr/bin/python3
"""
Module: rectangle
This module defines a Rectangle class.
"""

class Rectangle:
    """
    Represent a Rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializes a square with an optional size.
        
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width value"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle with validation.
        
        Args:
            value (int): The new width of the rectangle.
        
        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Get the height value"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle with validation.
        
        Args:
            value (int): The new width of the rectangle.
        
        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """Calculate perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)      

    def __str__(self):
        """Returns a string representation of the rectangle with '#' characters."""
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.width] * self.height)
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle to allow instance recreation
        using eval(). The string format is: Rectangle(width, height).
        """
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """Called when the instance is about to be deleted. Prints a message."""
        print("Bye rectangle...")
        