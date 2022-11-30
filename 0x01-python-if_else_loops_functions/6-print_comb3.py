#!/usr/bin/python3
for value1 in range(0, 9):
    for value2 in range(value1 + 1, 10):
        if value1 == 8:
            print("{:d}{:d}".format(value1, value2))
            break
        print("{:d}{:d}".format(value1, value2), end=", ")
