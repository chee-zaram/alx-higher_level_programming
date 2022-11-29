#!/usr/bin/python3

# Prints the ASCII alphabet in lowercase
for alpha in range(97, 123):
    if "{:c}".format(alpha) not in "qe":
        print("{:c}".format(alpha), end='')
