#!/usr/bin/python3
"""
Properties of a class.
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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = self.set_size(self, value)

    def area(self):
        return self.__size * self.__size
