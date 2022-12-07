#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Function to return the integer value of a number in roman numerals..

    Parameters:
        roman_string: String containing the roman numerals.

    Return:
        0 if argument is not a string or None.
    """

    try:
        roman_string = roman_string.upper()
    except AttributeError:
        return 0

    roman_dict = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    jump = False
    value = 0

    for idx in range(len(roman_string) - 1, -1, -1):
        if jump:
            jump = False
            continue

        if roman_string[idx] in roman_dict.keys():
            curr_num = roman_dict[roman_string[idx]]
            left_num = roman_dict[roman_string[idx - 1]]

            if idx == 0:
                left_num = 1001
            if curr_num > left_num:
                jump = True
                value += (curr_num - left_num)
            else:
                value += curr_num

    return value
