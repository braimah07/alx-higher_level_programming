#!/usr/bin/python3
"""A module that defines a square"""


class Square:
    """Defines a Square"""

    def __init__(self, size=0):
        """Initializing Square Size
        Args:
            size: represents the size of the square definition
        Raises:
            TypeError: when size is not an integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        """Function to Retrive Size of Square"""

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        Calculate area of the square
        Returns: The square of the size
        """

        return self.__size ** 2
