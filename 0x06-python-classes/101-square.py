#!/usr/bin/python3
"""A module with definition of a class `Square`"""


class Square:
    """A class that defines a square by private, public instance attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the intance attribute and raises exception if error

        Args:
            size (int): Size of the square
            position (tuple): A tuple of two positive number for x and y axis
        """
        Square.check_size(size)
        self.__size = size

        Square.check_pos(position)
        self.__position = position

    @property
    def size(self):
        """:obj:`int`: Current size of the square

        The setter method raises an exception if the value is not int or < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        Square.check_size(value)
        self.__size = value

    def area(self):
        """Method that returns the current area of the square"""
        return self.__size ** 2

    @property
    def position(self):
        """:obj:`tuple` of :obj:`int`: index 0 sets spaces and 1 sets newline

        The setter method raises an exception of ValueError or TypeError
        """
        return self.__position

    @position.setter
    def position(self, value):
        Square.check_pos(value)
        self.__position = value

    def my_print(self):
        """Prints the square using `#` signs"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Returns the square made using `#` signs"""

        sq_str = ""
        if self.__size == 0:
            return sq_str
        else:
            x, y = self.__position

            for _ in range(y):
                sq_str = sq_str + "\n"

            for _ in range(self.__size):
                if x:
                    sq_str = sq_str + (' ' * x)
                sq_str += ('#' * self.__size) + '\n'
            sq_str = sq_str[:-1]
            return sq_str

    @staticmethod
    def check_size(size):
        """Checks if the size passed to class Square is valid

        Args:
            size (int): The size of the square at a given instance
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @staticmethod
    def check_pos(position):
        """Checks if the position passed to class Square is valid

        Args:
            position: The position at which the square should be printed
        """

        if type(position) != tuple or len(position) != 2 \
            or type(position[0]) != int or type(position[1]) != int \
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
