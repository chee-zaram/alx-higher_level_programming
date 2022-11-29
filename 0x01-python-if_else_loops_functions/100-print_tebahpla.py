#!/usr/bin/python3

# Prints ASCII alphabet in reverse order, alternating lower and uppercase
for alpha in range(122, 96, -1):
    print("{:c}".format(alpha) if alpha % 2 == 0
          else "{:c}".format(alpha - 32), end='')
