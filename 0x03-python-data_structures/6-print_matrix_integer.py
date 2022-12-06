#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    prints a matrix of integers to STDOUT
    """
    for row in matrix:
        row_len = len(row)
        for f in range(row_len):
            if f != row_len - 1:
                print("{:d}".format(row[f]), end=' ')
            else:
                print("{:d}".format(row[f]), end='')
        print()
