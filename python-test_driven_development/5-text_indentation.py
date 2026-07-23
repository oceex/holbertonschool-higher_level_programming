#!/usr/bin/python3


"""
hi
hi

"""


def text_indentation(text):
    """ finalllyyyyyyyyy """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    a = text.split('.')
    for m in range(len(a)):
        b = a[m].split(':')
        if not m == 0:
            print('.', end="\n\n")
        for n in range(len(b)):
            c = b[n].split('?')
            if not n == 0:
                print(':', end="\n\n")
            for o in range(len(c)):
                if not o == 0:
                    print('?', end="\n\n")
                print(c[o].strip(), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
