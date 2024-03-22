#!/usr/bin/python3

def roman_to_int(roman_string):
    dict_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    tot = 0
    val = 0
    prev = 0
    idx = 0
    if (not isinstance(roman_string, str) or roman_string is None):
        return (0)
    for i in roman_string:
        if dict_r.get(roman_string[idx], 0) == 0:
            return (0)
        val = dict_r[i]
        if val > prev:
            tot = tot - prev
            tot = tot + val - prev
        else:
            tot += val
        prev = val
        idx += 1
    return (tot)
