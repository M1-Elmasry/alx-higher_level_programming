#!/usr/bin/python3


def roman_to_int(roman_string):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if roman_string is None:
        return None

    result = 0

    for i in range(len(roman_string) - 1):
        if values[roman_string[i]] < values[roman_string[i + 1]]:
            result -= values[roman_string[i]]
        elif roman_string[i] in values.keys():
            result += values[roman_string[i]]

    result += values[roman_string[-1]]

    return result
