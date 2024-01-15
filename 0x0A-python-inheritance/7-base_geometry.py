#!/usr/bin/python3
"""Class defined"""


class BaseGeometry:
    '''Class represents BaseGeometry'''

    def area(self):
        '''method not implemented yet'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates an integer value'''
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
