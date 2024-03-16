#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
	a = len(matrix)
	b = 0
	if a == 1 and len(matrix[0]) == 0:
		print()
	while (a >= b + 1):
		for i in matrix[b]:
			if i == matrix[b][-1]:
				print("{:d}".format(i))
			else:
				print("{:d} ".format(i), end="")
		b += 1
