#!/usr/bin/python3
"""
Divides Two lists
"""


def list_division(my_list_1, my_list_2, list_length):
    """
    divides the first list with the second one.
    """
    i = 0
    list_ = []
    while i < list_length:
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            list_.append(a / b)
        except IndexError:
            print("out of range")
            list_.append(0)
        except ZeroDivisionError:
            print("division by 0")
            list_.append(0)
        except TypeError:
            print("wrong type")
            list_.append(0)
        i = i + 1
    return (list_)
