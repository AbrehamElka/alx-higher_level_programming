#!/usr/bin/python3
def uniq_add(my_list=[]):
	total = 0
	set_list = set(my_list)
	for i in set_list:
		total += i
	return (total)
