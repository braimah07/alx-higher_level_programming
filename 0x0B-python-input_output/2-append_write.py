#!/usr/bin/python3
'''Module that appends text to a file'''


def append_write(filename="", text=""):
    '''Function that appends texts to a file and returns number of chars'''
    with open(filename, 'a', encoding='utf-8') as f:
        no_chars = f.write(text)
        return no_chars
