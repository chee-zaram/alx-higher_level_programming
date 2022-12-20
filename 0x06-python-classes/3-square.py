#!/usr/bin/python3
"""A module that has definition of a class Square"""


class Square:
    """A class that defines a square by private, public instance attribute
    """

    def __init__(self, size=0):
        """Initializes the intance private attribute"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Method that returns the current area of the square"""
        return self.__size ** 2
