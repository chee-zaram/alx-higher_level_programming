#!/usr/bin/python3
"""The ``101-lazy_matrix_mul.`` module

This module contains the ``lazy_matrix_mul`` function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        Product of the two matrices
    """

    return np.matmul(m_a, m_b)
