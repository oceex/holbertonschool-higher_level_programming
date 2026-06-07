#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)
    sa, sb = 0, 0
    if a >= 2:
        sa = tuple_a[0] + tuple_a[1]
    elif a == 1:
        sa = tuple_a[0]

    if b >= 2:
        sb = tuple_b[0] + tuple_b[1]
    elif b == 1:
        sb = tuple_b[0]

    tuple = (sa, sb)
    return tuple
