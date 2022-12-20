#!/usr/bin/python3
Square = __import__("3-square").Square

my_sq = Square(3)
print("Area: {}".format(my_sq.area()))

try:
    print(my_sq.size)
except Exception as e:
    print(e)

try:
    print(my_sq.__size)
except Exception as e:
    print(e)

my_sq_2 = Square(5)
print("Area: {}".format(my_sq_2.area()))
