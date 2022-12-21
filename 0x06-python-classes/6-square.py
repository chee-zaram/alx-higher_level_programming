#!/usr/bin/python3
"""A module that has definition of a class Square"""


class Square:
    """A class that defines a square by private, public instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the intance attribute and raises exception if error

        Args:
            size (int): Size of the square
            position (tuple): A tuple of two positive number for x and y axis
        """
        check_size(size)
        self.__size = size

        check_pos(position)
        self.__position = position

    @property
    def size(self):
        """:obj:`int`: Current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        check_size(value)
        self.__size = value

    def area(self):
        """Method that returns the current area of the square"""
        return self.__size ** 2

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: index 0 sets spaces and 1 sets newline
        """
        return self.__position

    @position.setter
    def position(self, value):
        check_pos(value)
        self.__position = value

    def my_print(self):
        """Prints the square using `#` signs"""
        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            for _ in range(y):
                print()
            for _ in range(self.__size):
                if x:
                    print(' ' * x, end='')
                print('#' * self.__size)


def check_size(size):
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")


def check_pos(position):
    if type(position) != tuple or len(position) != 2 \
        or type(position[0]) != int or type(position[1]) != int \
            or position[0] < 0 or position[1] < 0:
        raise TypeError("position must be a tuple of 2 positive integers")
