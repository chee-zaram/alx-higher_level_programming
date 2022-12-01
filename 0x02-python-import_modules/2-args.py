#!/usr/bin/python3

# Program to display the command line arguments passed to the program
def simp_print_args():
    from sys import argv

    argc = len(argv)
    if argc == 1:
        print("0 arguments.")
    else:
        if argc == 2:
            header = "{:d} argument:".format(argc - 1)
        else:
            header = "{:d} arguments:".format(argc - 1)
        print(header)
        for i in range(1, argc):
            print("{:d}: {}".format(i, argv[i]))


if __name__ == "__main__":
    simp_print_args()
