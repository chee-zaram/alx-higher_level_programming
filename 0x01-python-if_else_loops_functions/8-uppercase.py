#!/usr/bin/python3

# Function to print a string in uppercase
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            char = ord(i) - 32
        else:
            char = ord(i)
        print("{:c}".format(char), end='')
    print()
