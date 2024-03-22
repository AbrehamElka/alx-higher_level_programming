#!/usr/bin/python3

def roman_to_int(roman_string):
	dict_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	tot = 0
	val = 0
	prev = 0
	jump = False
	for i in roman_string:
		val = dict_r[i]
		if val > prev and not jump:
			tot = tot - prev
			tot = tot + val - prev
			jump = True
		else:
			tot += val
			jump = False
		prev = val
	return (tot)
