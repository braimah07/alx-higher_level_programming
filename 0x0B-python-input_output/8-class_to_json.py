#!/usr/bin/python3
'''Module'''


def class_to_json(obj):
    '''Returns Dictionary Description with Simple Data Structure'''
    '''    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[key] = value
    return json_dict'''
    '''Another method is just one line below'''
    return obj.__dict__
