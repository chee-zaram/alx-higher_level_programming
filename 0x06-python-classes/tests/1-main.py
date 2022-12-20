#!/usr/bin/python3
Square = __import__("1-square").Square

my_sq = Square(12)
print(type(my_sq))
print(my_sq.__dict__)

try:
    print(my_sq.size)
except Exception as ex:
    print(ex)

try:
    print(my_sq.__size)
except Exception as ex:
    print(ex)
