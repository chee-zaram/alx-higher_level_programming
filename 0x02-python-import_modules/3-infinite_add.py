#!/usr/bin/python3

# Adds all whole numbers passed as command line arguments to the program
def simp_add_arg():
    from sys import argv

    result = 0
    for num in argv[1:]:
        result += int(num)
    print(result)


if __name__ == "__main__":
    simp_add_arg()
