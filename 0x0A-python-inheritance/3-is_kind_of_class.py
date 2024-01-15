#!/usr/bin/python3
"""
    Checks if object is an instance of a clas, or an inherited class
"""


def is_kind_of_class(obj, a_class):
    """returns true if object is an instance of a class"""
    return (isinstance(obj, a_class))
