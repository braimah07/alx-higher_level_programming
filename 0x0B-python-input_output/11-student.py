#!/usr/bin/python3
'''Module'''


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns dictionary representation'''
#        for items in attrs:
#        if isinstance (attrs, str):
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attribhutes of the Student"""
        for k, v in json.items():
            setattr(self, k, v)
