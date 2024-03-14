#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	a = len(argv)
	b = 0
	if a == 1:
		print("0 arguments.")
	else:
		if a > 2:
			print("{} arguments:".format(a - 1))
		else:
			print("1 argument:")
		while(a > 1):
			print("{}: {}".format(b + 1, argv[b + 1]))
			b += 1
			a -= 1
