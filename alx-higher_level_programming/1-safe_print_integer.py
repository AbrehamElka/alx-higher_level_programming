#!/usr/bin/python3
"""
Safe Integer printer
"""


def safe_print_integer(value):
    """
    prints value if it is an integr
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as err:
        return False
