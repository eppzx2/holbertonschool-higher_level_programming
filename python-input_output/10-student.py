#!/usr/bin/python3
"""
Defines a Student class with json
"""


class Student:
    """
    class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            # Return all attributes
            return self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            filtered = {}
            for key in attrs:
                if key in self.__dict__:
                    filtered[key] = self.__dict__[key]
            return filtered
        return self.__dict__.copy()
