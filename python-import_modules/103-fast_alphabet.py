#!/usr/bin/python3
wow = lambda a=90: a >= 65 and (wow(a - 1), print(chr(a), end=(str())[0:0]))[1]
wow() or print()
