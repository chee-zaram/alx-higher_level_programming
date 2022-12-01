#!/usr/bin/python3

# Imports functions from a module and uses them to perform basic operations
# on integers passed as commandline arguments
def simp_cmdLine_calc():
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    if len(op) != 1 or op not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{:d} {} {:d} = {:d}".format(a, op, b, result))


if __name__ == "__main__":
    simp_cmdLine_calc()
