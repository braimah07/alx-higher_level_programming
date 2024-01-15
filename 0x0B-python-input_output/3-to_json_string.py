#!/usr/bin/python3
'''Module to convert data to json'''


import json


def to_json_string(my_obj):
    '''Returns json representation of an input'''
    return (json.dumps(my_obj))
