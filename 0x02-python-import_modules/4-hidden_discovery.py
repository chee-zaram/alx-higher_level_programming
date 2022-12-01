#!/usr/bin/python3

# Prints out all the names defined by the given compiled module below
if __name__ == "__main__":
    hidden_4 = __import__("hidden_4")

    defNames = dir(hidden_4)
    for name in defNames:
        if name[:2] not in "__":
            print(name)
