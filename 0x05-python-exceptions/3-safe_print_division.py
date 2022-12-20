#!/usr/bin/python3


def safe_print_division(a, b):
    """
    divides two integers and prints the result
    catches divide by zero exception
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {:d}".format(result))
    return (result)
