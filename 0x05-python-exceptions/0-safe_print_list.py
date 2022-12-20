#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints a list of anything, but only prints the integers
    Returns the amount of integers printed
    """
    number_of_element = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            number_of_element += 1
        except:
            continue
    print()
    return number_of_element
