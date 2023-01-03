#!/usr/bin/python3
"""This is the "0-matrix_divided" module.

This module supplies one function, matrix_divided.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Args:
        matrix (List[List[Union[int, float]]]): The matrix to divide.
        div (Union[int, float]): The number to divide by.

    Returns:
        List[List[float]]: The matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If any row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.

    Examples:
    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0
    """

    # checking if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    # checking if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # checking if it is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # checking if all rows are the same length
    row_lens = [len(row) for row in matrix]
    if not all(curr_len == row_lens[0] for curr_len in row_lens):
        raise TypeError("Each row of the matrix must have the same size")

    # returning a list of lists
    return [[round(num / div, 2) for num in row] for row in matrix]
