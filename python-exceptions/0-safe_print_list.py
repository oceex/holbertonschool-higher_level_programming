#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    c = 0
    try:
        for n in my_list:
            print(f"{n}", end="")
            c += 1
        print()
    except IndexError:
        pass
    finally:
        return c
