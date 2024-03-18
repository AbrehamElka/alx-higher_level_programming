#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = len(my_list)
    y = 0
    new_l = []
    while ((y + 1) <= x):
        if my_list[y] % 2 == 0:
            new_l.append(True)
        else:
            new_l.append(False)
        y += 1
    return (new_l)
