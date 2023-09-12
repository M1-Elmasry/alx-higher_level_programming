#!/usr/bin/python3
"""representing a append_write function"""


def append_write(filename="", text=""):
    """append @text to @filename"""
    with open(filename, "a", encoding="UTF8") as file:
        n_chars = file.write(text)

        return n_chars
