#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	a = len(argv)
	b = 0
	if a == 2:
		print("1 argument\n1: {}".format(argv[a - 1]))
	else:
		print("{} arguments".format(a - 1))
		while(a > 1):
			print("{}: {}".format(b + 1, argv[b + 1]))
			b += 1
			a -= 1
