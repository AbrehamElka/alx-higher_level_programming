#!/usr/bin/python3
"""
Module 3-say_my_name
Contains one function that prints full name.
Name printer.
"""


def say_my_name(first_name, last_name=""):
    """
    Return: Nothing.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
