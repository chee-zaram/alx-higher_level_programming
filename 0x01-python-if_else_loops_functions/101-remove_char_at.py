#!/usr/bin/python3

# Removes a character at a specified index n
def remove_char_at(str, n):
    strCopy = ""
    for i in range(len(str)):
        if i == n:
            continue
        strCopy += str[i]
    return strCopy
