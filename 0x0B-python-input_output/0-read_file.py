#!/usr/bin/python3
'''A module to input file'''


def read_file(filename=""):
    '''Read file module'''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
