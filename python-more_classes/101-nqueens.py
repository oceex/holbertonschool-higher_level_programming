#!/usr/bin/python3
import sys


def queens(n):
    pass


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        c = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        exit(1)
    if c < 4:
        print("N must be at least 4")
        exit(1)
    queens(c)


main()
