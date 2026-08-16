#!/usr/bin/python3
"""Module that defines the LockedClass class."""


class LockedClass:
    """Prevent the user from dynamically creating new instance
    attributes, except for one called first_name.
    """

    __slots__ = ['first_name']