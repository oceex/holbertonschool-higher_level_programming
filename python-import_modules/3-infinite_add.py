#!/usr/bin/python3
import sys


def main():
    k = 0
    for i in range(1, len(sys.argv)):
        k += int(sys.argv[i])
    print(k)


if __name__ == "__main__":
    main()
