#!/usr/bin/python3

def multiple_returns(sentence):
    s = sentence
    return ((0, None) if (s is None or len(s) == 0) else (len(s), s[0]))
