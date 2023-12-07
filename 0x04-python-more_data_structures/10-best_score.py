#!/usr/bin/python3
def best_score(a_dictionary):
    """
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary.keys())

    if not a_dictionary:
        return None
    else:
        highest_key = None
        for key in a_dictionary:
            if highest_key is None or key > highest_key:
                highest_key = key
        return highest_key
    """
    if not a_dictionary:
        return None
    max_val = max(a_dictionary, key=lambda x: a_dictionary[x])
    return max_val
