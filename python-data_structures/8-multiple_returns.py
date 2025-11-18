#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        frst = None
    else:
        frst = sentence[0]
    return (len(sentence), frst)

