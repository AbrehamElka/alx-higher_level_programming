#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if number < 0:
	temp = number * -1
if temp % 10 > 5:
	print("Last digit of {} is {} and is greater than 5".format(number, temp % 10))
elif temp % 10 == 0:
	print("Last digit of {} is {} and is 0".format(number, temp % 10))
else:
	print("Last digit of {} is {} and is less than 6 and not 0".format(number, temp % 10))
