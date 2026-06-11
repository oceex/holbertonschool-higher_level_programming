#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    c, i = 0, 0
    while x > 0:
        try:
            print("{:d}".format(my_list[i]), end="")
            i, c += 1
            x -= 1
        except IndexError:
            print("IndexError: list index out of range")
            break
        except TypeError:
            i += 1
            continue
        except Exception:
            break
    print()
    return c
