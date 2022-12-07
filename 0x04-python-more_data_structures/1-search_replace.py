#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    replaces all occurances of search with replace
    """
    return ([element if element != search else replace for element in my_list])
