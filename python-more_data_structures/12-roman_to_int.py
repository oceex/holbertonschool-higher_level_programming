#!/usr/bin/python3


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'a': 0
            }
    most = "a"
    index = 0
    for i in range(len(roman_string)):
        if roman[roman_string[i]] > roman[most[0]]:
            most = roman_string[i]
            index = i
        elif roman[roman_string[i]] == roman[most[0]] and i - 1 == index:
            most += roman_string[i]
    s = roman_string.partition(most)
    boss = 0
    for n in most:
        boss += roman[n]
    if s[0] == '' and s[2] == '':
        return boss
    for i in range(len(s)):
        if i == 0:
            boss -= roman_to_int(s[i])
        elif i == 2:
            boss += roman_to_int(s[i])
    return boss
