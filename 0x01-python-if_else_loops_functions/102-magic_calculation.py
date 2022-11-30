#!/usr/bin/python3

# This function is a translation of a given bytecode
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
