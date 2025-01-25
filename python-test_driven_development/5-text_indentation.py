#!/usr/bin/python3
"""
This module defines the function `text_indentation` which prints a given 
text with two new lines after each of these characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each of the characters '.', '?', and ':'.
    
    Args:
        text (str): The text to be formatted.
    
    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    idx = 0
    while idx < len(text):
        if text[idx] in ['.', '?', ':']:
            print(text[idx], end="")
            print("\n")
            idx += 1
            while idx < len(text) and text[idx] == " ":
                idx += 1
        else:
            print(text[idx], end="")
            idx += 1
