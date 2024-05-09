#!/usr/bin/python3
"""
prints only integers.
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    prints integers for the max of x items
    """
    i = 0
    n = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            n = n + 1
        except TypeError:
            pass
        except ValueError:
            pass
        i = i + 1
    print()
    return (n)
