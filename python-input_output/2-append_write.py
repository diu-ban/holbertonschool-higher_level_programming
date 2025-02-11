#!/usr/bin/python3

"""
Module: append_write

This module provides a function to append a string to the end of a text file (UTF-8 encoded)
and return the number of characters added. If the file does not exist, it will be created.
"""

def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file (UTF-8 encoded) and returns the number of characters added.

    Args:
        filename (str): The path to the file where the text will be appended.
                       Defaults to an empty string.
        text (str): The string to be appended to the file. Defaults to an empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding = "utf-8") as f:
        return f.write(text)
    