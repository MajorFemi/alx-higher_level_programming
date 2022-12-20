#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
    takes two lists and creates a new list with result of divison
    operation
    handles errors and prints them to stdout
    """
    new_list = []
    result_of_div = 0
    for i in range(0, list_length):
        try:
            result_of_div = (my_list_1[i] / my_list_2[i])
        except TypeError:
            result_of_div = 0
            print("wrong type")
        except ZeroDivisionError:
            result_of_div = 0
            print("division by 0")
        except IndexError:
            result_of_div = 0
            print("out of range")
        finally:
            new_list.append(result_of_div)
    return new_list
