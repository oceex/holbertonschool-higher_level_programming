#!/usr/bin/python3
"""
k
k
"""


class Bird:
    def fly():
        print("The bird is flying")

    def habitat():
        print("The bird lives in the sky")

class Fish:
    def swim():
        print("The fish is swimming")

    def habitat():
        print("The fish lives in water")

class FlyingFish(Fish, Bird):
    def swim():
        print("The flying fish is swimming!")

    def fly():
        print("The flying fish is soaring!")

    def habitat():
        print("The flying fish lives both in water and the sky!")
