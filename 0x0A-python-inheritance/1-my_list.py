#!/usr/bin/pyton3
"""
Inherits List
"""


class MyList(list):
    """
    Inherits List
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
