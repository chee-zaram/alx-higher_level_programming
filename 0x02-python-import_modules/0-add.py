#!/usr/bin/python3

# Imports and uses a function from a module
def simp_add():
    from add_0 import add

    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    simp_add()
