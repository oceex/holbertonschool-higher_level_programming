#!/usr/bin/python3
i = 1
def magic_string():
    return "BestSchool" if i == 1 else "BestSchool, "*(i-1) + "BestSchool"
