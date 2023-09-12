#!/usr/bin/python3
"""representing a write_file function"""


def write_file(filename="", text=""):
    """overwrite @filename with @text"""
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
