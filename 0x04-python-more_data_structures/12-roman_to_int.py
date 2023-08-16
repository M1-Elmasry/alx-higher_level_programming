#!/usr/bin/python3


def roman_to_int(roman_string):
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900
    }
    values_keys = values.keys()

    if roman_string is None:
        return None

    if len(roman_string) == 1 and roman_string in values.keys():
        return values[roman_string]

    result = 0

    for i in range(1, len(roman_string)):
        two_chars = roman_string[i - 1] + roman_string[i]

        if two_chars in values_keys:
            result += values[two_chars]
            i += 1

        elif roman_string[i - 1] in values_keys:
            result += values[roman_string[i - 1]]

    if roman_string[-2] + roman_string[-1] not in values_keys:
        result += values[roman_string[-1]]

    return result

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCLXXXIX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))


