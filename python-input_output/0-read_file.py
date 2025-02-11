#!/usr/bin/python3

"""
Module: file_reader

This module provides a function to read and print the contents of a file.
It is designed to handle text files with UTF-8 encoding.
"""

def read_file(filename=""):
    """
    Reads and prints the contents of a file.

    Args:
        filename (str): The path to the file to be read. Defaults to an empty string.

    Returns:
        None: The function prints the file contents to the standard output.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there is an issue reading the file.
    """
    with open(filename, "r", encoding = "utf-8") as file:
        print(file.read())
