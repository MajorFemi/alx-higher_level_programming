#!/usr/bin/python3


def best_score(a_dictionary):
    """
    gets the best value from a dictionary (greatest integer)
    """
    biggest_val = 0
    score = None
    if type(a_dictionary) is dict:
        for key, value in a_dictionary.items():
            if value > biggest_val:
                biggest_val = value
                score = key
    return score
