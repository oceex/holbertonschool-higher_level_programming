#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)
    i0, i1 = 0, 0
    if a or b:
        if a:
            i0 += tuple_a[0]
        if b:
            i0 += tuple_b[0]
    if a >= 2 or b >= 2:
        if a >= 2:
            i1 += tuple_a[1]
        if b >= 2:
            i1 += tuple_b[1]
    return (i0, i1)
