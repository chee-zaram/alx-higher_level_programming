#!/usr/bin/python3

def safe_print_integer_err(value):
    """Function that prints an integer"""

    from sys import stderr
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        stderr.write("Exception: {}\n".format(err))
        return False
