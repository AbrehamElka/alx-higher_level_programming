#!/usr/bin/python3
def max_integer(my_list=[]):
	x = 0
	y = 1
	if len(my_list) == 0:
		return (None)
	else:
		while (y != len(my_list)):
			if my_list[y-1] >= x:
				x = my_list[y-1]
			y += 1
		return (x)
