#!/usr/bin/python3
def new_in_list(my_list, idx, element):
	a = my_list[:]

	if idx < 0:
		return (my_list)
	if idx > len(a) - 1:
		return (my_list)
	a[idx] = element
	return (a)
