#!/usr/bin/python3
"""
abc
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    " abc class "
    @abstractmethod
    def sound(self):
        " an abstract method "
        pass

class Cat(Animal):
    " caca "
    def sound(self):
        " implementing method "
        return "Meow"

class Dog(Animal):
    " dada "
    def sound(self):
        " implementing method "
        return "Bark"

