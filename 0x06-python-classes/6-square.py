#!/usr/bin/python3
"""
Square class.
"""


class Square:
    """
    A square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = self.set_size(self, size)
        self.__position = self.set_pos(self, position)

    @staticmethod
    def set_pos(self, value):
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int) or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        return value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.position = set_pos(self, value)

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

    def my_print(self):
        if self.size == 0:
            print()
            return
        [print() for i in range(0, self.position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for i in range(0, self.position[0])]
            for i in range(0, self.size):
                print("#", end="")
            print()
