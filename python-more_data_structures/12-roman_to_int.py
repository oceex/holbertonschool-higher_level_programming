#!/usr/bin/python3


def roman_to_int(roman_string):
    if not type(roman_string) == type("leen"):
        return 0

    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'a': 0}
    most = "a"
    for n in roman_string:
        if roman[n] > roman[most[0]]:
            most = n
        elif roman[n] == roman[most[0]]:
            most += n
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
