#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Returns a tuple with the length of a string and its first
    character
    """
    sen_len = len(sentence)
    if sen_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
    return ((sen_len, first_char))
