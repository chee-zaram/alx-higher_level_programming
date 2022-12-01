#!/usr/bin/python3

def magic_calculation(a, b):
    """My magic calculation function

    Translated from bytecode
    Makes use of add() and sub() functions from magic_calculation_102 module

    Args:
        a: first integer
        b: second integer

    Returns:
        The resulting value of sub(a, b) or c
    """
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
    else:
        return sub(a, b)

    for i in range(4, 6):
        c = add(c, i)
    return c
