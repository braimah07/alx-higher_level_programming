#!/usr/bin/python3
'''Module to convert Json to object'''


import json


def from_json_string(my_str):
    '''Returns object from json representation'''
    return (json.loads(my_str))
