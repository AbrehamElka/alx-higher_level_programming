#!/usr/bin/python3
for i in range(26):
	if chr(i + 97) == 'q' or chr(i + 97) == 'e':
		continue
	print("{}".format(chr(i + 97)), end="")
