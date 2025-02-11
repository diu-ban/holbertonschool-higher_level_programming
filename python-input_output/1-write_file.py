#!/usr/bin/python3

"""
Module: file_writer

This module provides a function to write text to a file.
It is designed to handle text files with UTF-8 encoding.
"""

def write_file(filename="", text=""):
    """
    Writes a string to a file.

    Args:
        filename (str): The path to the file where the text will be written.
                         Defaults to an empty string.
        text (str): The string to be written to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written to the file.

    Raises:
        IOError: If there is an issue writing to the file.
    """
    with open(filename, "w", encoding = "utf-8") as f:
        return f.write(text)
