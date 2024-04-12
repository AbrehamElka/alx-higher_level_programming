#!/usr/bin/python3
"""
Module 4-print_square
Contains one function to create a square
Square Creator
"""


def print_square(size):
    """
    Return: Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print()
