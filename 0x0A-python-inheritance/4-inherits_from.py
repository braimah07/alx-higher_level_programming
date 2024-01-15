#!/usr/bin/python3
"""
    Checks if object is an instane of a class
"""


def inherits_from(obj, a_class):
    """Returns true if object is an instance of inherited class, or false"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
