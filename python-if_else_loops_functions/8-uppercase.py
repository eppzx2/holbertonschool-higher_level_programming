#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= c <= 'z': 
            print("{:c}".format(chr(ord(c) - 32)), end="")
        else:  
            print("{:c}".format(c), end="")
    print() 
