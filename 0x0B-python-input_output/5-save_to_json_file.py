#!/usr/bin/python3
'''Module'''


import json


def save_to_json_file(my_obj, filename):
    '''Function writes an Objet to a textfile using JSON'''
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
