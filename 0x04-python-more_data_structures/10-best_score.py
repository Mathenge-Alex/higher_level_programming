#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Check Key for Max value in a dictionary
    """
    if a_dictionary is None:
        return None

    best_score = max(a_dictionary.values(), default=None)
    for j, k in a_dictionary.items():
        if k == best_score:
            return j
