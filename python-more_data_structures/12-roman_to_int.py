#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    total = 0
    lenght = len(roman_string)
    for i in range(lenght):
        value = roman_dic[roman_string[i]]
        if i + 1 < lenght and value < roman_dic[roman_string[i + 1]]:
            total -= value
        else:
            total += value
    return total
