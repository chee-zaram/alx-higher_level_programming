#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function to print the first x elements of a list of only integers

    IndexError is not taken care of
    """

    leng = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end='')
            leng += 1
        except (ValueError, TypeError):
            pass
    print()
    return leng
