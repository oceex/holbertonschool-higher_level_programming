#!/usr/bin/python3


def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'a': 0}
    most = "a"
    for n in roman_string:
        if roman[n] > roman[most[0]]:
            most = n
        elif roman[n] == roman[most[0]]:
            most += n
    s = roman_string.partition(most)
    boss = 0
    for i in range(len(s)):
        for n in s[i]:
           if i == 0:
               boss -= roman[n]
           else:
               boss += roman[n]
    return boss
