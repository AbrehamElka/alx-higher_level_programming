#!/usr/bin/python3
def no_c(my_string):
	a = list(my_string)
	x = 0

	for i in a:
		if i == 'c' or i == 'C':
			a.pop(x)
			x -= 1
		x += 1
	my_string = ''.join(a)
	return (my_string)
