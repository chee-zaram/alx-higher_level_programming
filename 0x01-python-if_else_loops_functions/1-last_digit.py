#!/usr/bin/python3
import random

# Gives details about the last digit of a number
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
if number < 0:
    lastDigit *= -1
if lastDigit > 5:
    message = "and is greater than 5"
elif lastDigit == 0:
    message = "and is 0"
elif lastDigit < 6 and not 0:
    message = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d} {}".format(number, lastDigit, message))
