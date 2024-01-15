#!/usr/bin/python3
"""
    Module returns the list of available attributes
"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    attrs = dir(obj)
    # Return the list of attributes
    return attrs
