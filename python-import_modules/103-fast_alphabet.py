#!/usr/bin/python3
wow = lambda a=90: (wow(a - 1) if a > 65 else None, print(chr(a), end=""))[1]
print(wow() or "\n", end="")
