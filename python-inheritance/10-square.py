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
        
class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle object.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Validates both width and height using the integer_validator method 
        from the BaseGeometry class.

        Raises:
            TypeError: If either width or height is not an integer.
            ValueError: If either width or height is less than or equal to 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle object.

        The format is: "[Rectangle] <width> - <height>"

        Returns:
            str: A string representing the Rectangle object.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        The area is calculated as: width * height.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
    
class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): The size of the Square.
    """

    def __init__(self, size):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.

        Validates the size using the integer_validator method from the 
        BaseGeometry class and ensures that the size is a positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        The area of the square is calculated as: size * size.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size    