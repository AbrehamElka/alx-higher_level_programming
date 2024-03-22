#!/usr/bin/python3

def roman_to_int(roman_string):
	dict_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	index = 0
	jump = False
	tot = 0
	temp = 0
	len_str = len(roman_string)

	for i in roman_string:
		if index + 1 < len_str:
			if dict_r[i] < dict_r[roman_string[index + 1]] or jump:
				if jump:
					index += 1
					jump = False
					continue
				else:
					jump = True
				temp = dict_r[roman_string[index + 1]] - dict_r[i]
				tot += temp
				index += 1
				continue
		tot += dict_r[i]
		index += 1

	return (tot)
