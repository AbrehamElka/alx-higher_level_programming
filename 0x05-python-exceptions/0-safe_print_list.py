#!/usr/bin/python3
"""
Safe List Printer
"""


def safe_print_list(my_list=[], x=0):
    """
    prints a list to the number of x items.
    """

    try:
        i = 0
        for item in my_list:
            if i + 1 <= x:
                print(my_list[i], end="")
                i = i + 1
        print()
        return (i)
    except Exception as err:
        for item in my_list:
            print(item, end="")
        print()
        return (x)
