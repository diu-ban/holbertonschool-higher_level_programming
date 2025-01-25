#!/usr/bin/python3
"""
This module defines the function `matrix_divided` that divides all elements of a matrix by a given divisor.
"""
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.
    
    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor to divide each element in the matrix.
    
    Returns:
        list of lists: A new matrix with all elements divided by div, rounded to 2 decimal places.
    
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If rows of the matrix do not have the same size.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element of the matrix by div and round to 2 decimal places
    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    
    return new_matrix
