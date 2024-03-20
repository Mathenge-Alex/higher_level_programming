#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    converted_num = 0
    last = 0

    for dig_letter in roman_string:
        for numeral in roman_letters:
            if dig_letter == numeral[0]:
                if last == 0 or last >= numeral[1]:
                    converted_num += numeral[1]
                elif last < numeral[1]:
                    converted_num += numeral[1] - (last * 2)

                last = numeral[1]

    return converted_num
