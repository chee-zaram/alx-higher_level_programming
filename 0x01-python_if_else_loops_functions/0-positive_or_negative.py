#!/usr/bin/python3
import random

# Prints whether a randomly generated integer is negative, positive, or 0
number = random.randint(-10, 10)
if number > 0:
    print(number, "is positive")
elif number == 0:
    print(number, "is zero")
else:
    print(number, "is negative")
