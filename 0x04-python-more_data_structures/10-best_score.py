#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is not None and len(a_dictionary.keys()) > 0:
        sorted_dict = sorted(a_dictionary.items(), key=lambda a: a[1])
        max_val_key = sorted_dict[-1][0]
        return max_val_key
    else:
        return None
