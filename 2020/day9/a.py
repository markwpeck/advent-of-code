#!/usr/bin/env python3
from datetime import datetime

startTime = datetime.now()

def is_invalid(num, window):
	for astr in window:
		a = int(astr.rstrip())
		for bstr in window:
			b = int(bstr.rstrip())
			if num == (a + b):
				return False
	return True

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
input = open("input.txt", "r").readlines()
window = 25
for i in range(window,len(input)):
	available_numbers = input[i - window:i]
	if is_invalid(int(input[i]),available_numbers):
		print("{} is invalid".format(int(input[i])))

print(datetime.now() - startTime)