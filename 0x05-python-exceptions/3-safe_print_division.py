#!/usr/bin/python3

def safe_print_division(a, b):
    """Function to divide 2 integers and print the result

    TypeError is not taken care of
    """

    try:
        res = a / b
    except ZeroDivisionError:
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
