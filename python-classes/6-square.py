#!/usr/bin/python3
"""Module that defines a Square class."""


class Square:
    """Represents a square with a given size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with an optional size and position.
        
        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size  # Uses the property setter for validation
        self.position = position  # Uses the property setter for validation

    @property
    def size(self):
        """Gets the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.
        
        Args:
            value (int): The new size of the square.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Gets the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square with validation.
        
        Args:
            value (tuple): A tuple containing two positive integers.
        
        Raises:
            TypeError: If position is not a tuple of two positive integers.
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the `#` character considering position."""
        if self.__size == 0:
            print("")
            return

        # Print the vertical position (new lines)
        for _ in range(self.__position[1]):
            print("")

        # Print the square with horizontal offset
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
