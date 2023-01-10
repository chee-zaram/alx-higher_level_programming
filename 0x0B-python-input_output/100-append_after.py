#!/usr/bin/python3
"""Module ``100-append_after``"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line with a specific string

    Args:
        filename (str): Name of file to write to
        search_string (str): String to search for
        new_string (str): String to append after each line with `search_string`
    """
    if not search_string or not new_string:
        return

    with open(filename, 'r+', encoding="utf-8") as f:
        file_list = f.readlines()

    with open(filename, 'w') as fo:
        file_str = ""
        for line in file_list:
            file_str += line
            if search_string in line:
                file_str += new_string
        fo.write(file_str)
