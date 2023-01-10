#!/usr/bin/python3
"""Module ``12-pascal_triangle``"""


def pascal_triangle(n):
    """Returns a list of lists of ints representing the Pascal's triangle

    Args:
        n (int): The length of the triangle

    Return:
        Returns the triangle in a list of lists
    """
    if type(n) is not int:
        raise TypeError("n must be an int")

    a_list = []
    if n <= 0:
        return a_list

    a_list = [[1 for x in range(idx + 1)] for idx in range(n)]

    for rowIdx in range(2, n):
        for colIdx in range(1, rowIdx + 1):
            if colIdx < len(a_list[rowIdx - 1]):
                a_list[rowIdx][colIdx] = a_list[rowIdx - 1][colIdx - 1] + \
                        a_list[rowIdx - 1][colIdx]

    return a_list
