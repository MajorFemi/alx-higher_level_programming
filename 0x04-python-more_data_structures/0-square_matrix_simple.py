#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    """
    Compute the square value of all integers of a matrix
    """
    return ([[(f**2) for f in row] for row in matrix])
