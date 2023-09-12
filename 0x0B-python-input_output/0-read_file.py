#!/usr/bin/python3
"""representing a read_file function"""


def read_file(filename=""):
    """print @filename content"""
    with open(filename, "r", encoding="UTF8") as file:
        lines = file.readlines()
        for line in lines:
            print(line, end="")
