#!/usr/bin/python3
'''Module'''


import json


def load_from_json_file(filename):
    '''Function loads an Objet from a JSON file'''
    with open(filename, 'r') as f:
        obj = json.load(f)
    return obj
