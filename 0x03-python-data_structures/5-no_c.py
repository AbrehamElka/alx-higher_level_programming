#!/usr/bin/python3
def no_c(my_string):
    a = []
    x = 0
    for i in my_string:
        if i in 'cC':
            continue
        a.append(i)
        a = ''.join(a)
    return (a)
