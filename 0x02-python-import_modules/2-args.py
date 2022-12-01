#!/usr/bin/python3

# Program to display the command line arguments passed to the program
if __name__ == "__main__":
    from sys import argv

    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    elif argc > 1:
        print("{:d} arguments:".format(argc - 1))
        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))
