#!/usr/bin/python3
"""
Module 2-matrix_divided
contains one function that divides  a matrix with a num.
Matrix Divider.
"""


def matrix_divided(matrix, div):
    """
    Returns: A Matrix(matrix/div).
    """

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if isinstance(matrix, list):
        for item in matrix:
            if not isinstance(item, list):
                raise TypeError(msg)
            for i in item:
                if not isinstance(i, (int, float)):
                    raise TypeError(msg)
    len_row = len(matrix[0])
    mat = []

    for item in matrix:
        temp_li = []
        if len(item) != len_row:
            raise TypeError("Each row of the matrix must have the same size")
        for i in item:
            i = i / div
            temp_li.append(round(i, 2))
        mat.append(temp_li)
    return mat
