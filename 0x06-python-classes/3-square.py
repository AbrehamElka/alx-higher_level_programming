#!/usr/bin/python3
"""
An area calculator
"""


class Square:
    """
    A square class.
    """
    def __init__(self, size=0):
        self.__size = self.set_size(self, size)

    @staticmethod
    def set_size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return value

    def area(self):
        return self.__size * self.__size
