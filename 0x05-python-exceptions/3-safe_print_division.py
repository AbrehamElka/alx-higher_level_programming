#!/usr/bin/python3
"""
Divisor function
"""


def safe_print_division(a, b):
    """
    divides two numbers.
    """
    try:
        tot = a / b
    except ZeroDivisionError:
        tot = None
    finally:
        print("Inside result: {}".format(tot))
    return (tot)
