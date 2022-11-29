#!/usr/bin/python3

# Function that checks for lowercase character
def islower(c):
    for i in range(97, 123):
        if ord(c) == i:
            return True
    else:
        return False
