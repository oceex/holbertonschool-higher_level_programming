#!/usr/bin/python3
"""
k k kkk kk kk
"""


def append_after(filename="", search_string="", new_string=""):
    " k kkk k k k "
    with open(filename, "r") as x:
        v = x.read()
    x = v.split('\n')
    c = 0
    while c < len(x):
        for n in range(c, len(x)):
            if search_string in x[n]:
                x.insert(n+1, new_string)
                c = n + 2
                break
            else:
                c += 1
    m = '\n'.join(x)
    with open(filename, "w") as z:
        z.write(m)
