#!/usr/bin/python3
"""
inheritance training
"""


def inherits_from(obj, a_class):
    """inherited from the specified class"""
    return type(obj) is not a_class and isinstance(obj, a_class)
