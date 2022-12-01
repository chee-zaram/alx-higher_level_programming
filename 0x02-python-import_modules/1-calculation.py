#!/usr/bin/python3

# Imports functions from module and performs operations with them
def simp_calc():
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))


if __name__ == "__main__":
    simp_calc()
