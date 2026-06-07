#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer


def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    for n in my_list:
        print("{:d}".format(n))
