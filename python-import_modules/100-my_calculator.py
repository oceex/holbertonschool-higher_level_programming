#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = sys.argv[2]

    if op not in ["+", "-", "*", "/"]:
        print("Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    c = {
     "+": add,
     "-": sub,
     "*": mul,
     "/": div
    }

    print("{} {} {} = {}".format(a, op, b, c[op](a, b)))

    exit(0)

if __name__ == "__main__":
    main()
