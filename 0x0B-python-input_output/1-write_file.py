#!/usr/bin/python3
'''Module that writes text to a file'''


def write_file(filename="", text=""):
    '''Function that writes texts to a file and returns number of chars'''
    with open(filename, 'w', encoding='utf-8') as f:
        no_chars = f.write(text)
        return no_chars
