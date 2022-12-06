#!/bin/usr/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    new_tuple = ()
    for f in range(2):
        if f >= len_a:
            a = 0
        else:
            a = tuple_a[f]
        if f >= len_b:
            b = 0
        else:
            b = tuple_b[f]

        if (f == 0):
            new_tuple = (a + b)
        else:
            new_tuple = (new_tuple, a + b)
    return (new_tuple)
