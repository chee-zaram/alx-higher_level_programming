#!/usr/bin/python3

# Function to print a string in uppercase
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char = ord(str[i]) - 32
        else:
            char = ord(str[i])
        print("{:c}".format(char), end='')
    print()
