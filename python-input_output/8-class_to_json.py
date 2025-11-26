#!/usr/bin/python3
"""
dict qaytarmalidi
"""


def class_to_json(obj):
    """json serialization"""

    return obj.__dict__.copy()
