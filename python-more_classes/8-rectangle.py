#!/usr/bin/python3
"""
Module: rectangle
This module defines a Rectangle class.
"""

class Rectangle:
    """
    Represent a Rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes a square with an optional size.
        
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        return "\n".join([str(Rectangle.print_symbol) * self.width] * self.height)
    
    def __repr__(self):
        """
        Returns a string representation of the rectangle to allow instance recreation
        using eval(). The string format is: Rectangle(width, height).
        """
        return f"Rectangle({self.width}, {self.height})"
    
    def __del__(self):
        """Called when the instance is about to be deleted. Prints a message."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles based on their area and returns the biggest.
        If both have the same area, rect_1 is returned.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the bigger area, or rect_1 if areas are equal.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
