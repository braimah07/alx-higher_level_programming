#!/usr/bin/python3
"""
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_map={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = None

    for ch in roman_string:
        if ch not in roman_map:
            return 0

        value = roman_map[ch]
        if prev_value is not None and prev_value < value:
            result -= 2 * prev_value  # undo previous addition
        result += value
        prev_value = value

    return result
"""


def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    rom_dg = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        value = rom_dg[roman_string[i]]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
