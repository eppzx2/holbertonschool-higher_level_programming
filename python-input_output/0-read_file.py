#!/usr/bin/python3
"""
fayli acir oxuyur bagliyir
"""


def read_file(filename=""):
    """with ozu acir is bitende bagliyir f.close ehtiyac yoxdu"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
