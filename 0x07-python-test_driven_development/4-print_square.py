#!/usr/bin/python3
"""This is the ``4-print_square`` module

It contains the lone function ``print_square`` that prints a square using `#`
"""


def print_square(size):
    """Prints a square using `#`

    Args:
        size(int): The size of the square to print

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than zero
    """

    # make sure size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # make sure size is a valid value
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
