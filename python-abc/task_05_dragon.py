#!/usr/bin/python3
"""
k
k
"""

class SwimMixin:
    " s "
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    " f "
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    " s X f "
    def roar(self):
        print("The dragon roars!")
