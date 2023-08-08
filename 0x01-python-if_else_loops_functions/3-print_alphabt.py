#!/usr/bin/python3
for c in range(97, 123):
    char = chr(c)
    if char not in "qe":
        print("{}".format(char), end="")
