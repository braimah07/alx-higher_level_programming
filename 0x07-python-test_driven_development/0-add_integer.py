#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """ Function Returns Sum of Two (2) Integers
    Args:
        Int a, Int b

    Function Returns the Sum of Args
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    return a + b
