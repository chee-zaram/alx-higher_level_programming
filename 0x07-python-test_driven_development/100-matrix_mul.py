#!/usr/bin/python3
"""This is the ``100-matrix_mul`` module

It contains the lone function ``matrix_mul``
"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrice and returns the new_matrixing matrix

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The product of `m_a` and `m_b`.

    Raises:
        TypeError: If `m_a` or `m_b` is not a list,
            or if `m_a` or `m_b` is not a list of lists,
            or if one element of `m_a` or `m_b` is not an integer or a float,
            or if `m_a` or `m_b` is not a rectangle.
        ValueError: If `m_a` or `m_b` is empty,
            or if `m_a` and `m_b` can't be multiplied.

    Examples:
        >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        [[7, 10], [15, 22]]

        >>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
        [[13, 16]]

        >>> matrix_mul([[3], [5]], [[2, 3]])
        [[6, 9], [10, 15]]

        >>> matrix_mul([[1.5, 2.5], [3.5, 4.5]], [[5.5, 6.5], [7.5, 8.5]])
        [[27.0, 31.0], [53.0, 61.0]]

        >>> matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10]])
        Traceback (most recent call last):
            ...
        ValueError: m_a and m_b can't be multiplied

        >>> matrix_mul([[], []], [[5, 6], [7, 8]])
        Traceback (most recent call last):
            ...
        ValueError: m_a can't be empty
    """

    # make sure we are not dealing with None
    if m_a is None and m_b is None:
        return None

    # check that both arguments are of list type
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # make sure each matrix only contains list(s)
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # make sure the matrices are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # check that both matrices only contain integers or floats
    if not all(isinstance(n, (int, float)) for row in m_a for n in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n, (int, float)) for row in m_b for n in row):
        raise TypeError("m_b should contain only integers or floats")

    # get the length of each list in m_a and check m_a is a rectangle
    row_lens_in_a = [len(row) for row in m_a]
    if not all(curr_len == row_lens_in_a[0] for curr_len in row_lens_in_a):
        raise TypeError("each row of m_a must be of the same size")

    # get the length of each list in m_b and check m_b is a rectangle
    row_lens_in_b = [len(row) for row in m_b]
    if not all(curr_len == row_lens_in_b[0] for curr_len in row_lens_in_b):
        raise TypeError("each row of m_b must be of the same size")

    # make sure number of columns in m_a == rows in m_b
    if row_lens_in_a[0] != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # initialize the matrix to be returned
    new_matrix = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # for each of the list in m_a list
    for i in range(len(new_matrix)):
        # for each of the numbers in the current list
        for j in range(len(new_matrix[0])):
            # for each of the list in m_b
            for k in range(len(m_b)):
                # get the sum of the multiplication of each num in each row
                # in m_a by each num in the corresponding column in m_b
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
