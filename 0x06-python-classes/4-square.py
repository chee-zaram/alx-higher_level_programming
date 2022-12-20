#!/usr/bin/python3
"""A module that has definition of a class Square"""


class Square:
    """A class that defines a square by private, public instance attribute
    """

    def __init__(self, size=0):
        """Initializes the intance attribute and raises exception if error

        Args:
            size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """:obj:`int`: Current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Method that returns the current area of the square"""
        return self.__size ** 2
