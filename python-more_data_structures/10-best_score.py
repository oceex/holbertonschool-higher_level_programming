#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        best = next(iter(a_dictionary.values()))
    else:
        return None
    for n in a_dictionary:
        if a_dictionary[n] > best:
            best = a_dictionary[n]
    return best
