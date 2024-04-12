#!/usr/bin/python3
"""
Module 0-add_integer.
Contains one method that two numbers.
ADDING Calculator
"""


def add_integer(a, b=98):
    """
    Return: a + b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
