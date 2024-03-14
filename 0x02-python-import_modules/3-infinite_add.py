#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	a = len(argv)
	b = 0
	c = 0
	if a <= 1:
		print("0")
	else:
		while(a > 1):
			c += int(argv[b + 1])
			b += 1
			a -= 1
	print("{}".format(c))
