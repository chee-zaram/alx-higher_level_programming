#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Function to square every value in a 2D matrix.

    Parameters:
        matrix: Two dimensional matrix of integers.

    Return:
        The new matrix populated with the squares in the corresponding index.
    """

    if matrix:
        new_matrix = []
        for ls in matrix:
            new_matrix.append(list(map(lambda x: x ** 2, ls)))

    return new_matrix
