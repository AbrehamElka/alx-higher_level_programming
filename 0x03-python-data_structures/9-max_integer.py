#!/usr/bin/python3
def max_integer(my_list=[]):
    x = 0
    if my_list:
        x = my_list[0]
        for num in my_list:
            if num > x:
                x = num
        return (x)
    else:
        return (None)
