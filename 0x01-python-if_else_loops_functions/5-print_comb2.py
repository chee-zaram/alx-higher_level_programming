#!/usr/bin/python3

# Prints numbers from 0 to 99
for num in range(100):
    if num == 99:
        print("{:d}".format(num))
        break
    print("{:02d}".format(num), end=", ")
