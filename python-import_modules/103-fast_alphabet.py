#!/usr/bin/python3
class wow(int):__new__=lambda s,a=90:a>=65 and(wow(a-1),print(chr(a),end=str()))[1]
wow() or print()
