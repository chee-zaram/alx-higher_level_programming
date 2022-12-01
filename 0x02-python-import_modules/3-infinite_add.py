#!/usr/bin/python3

# Adds all whole numbers passed as command line arguments to the program
if __name__ == "__main__":
    from sys import argv

    result = 0
    for num in argv[1:]:
        result += int(num)
    print(result)
