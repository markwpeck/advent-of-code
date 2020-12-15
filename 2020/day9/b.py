#!/usr/bin/env python3
from datetime import datetime

startTime = datetime.now()

def is_invalid(num, window):
	for a in window:
		for b in window:
			if num == (a + b):
				return False
	return True

raw_input = open("input.txt", "r").readlines()
input = [int(x.rstrip()) for x in raw_input]
window = 25
target_num = 0
target_idx = 0
for i in range(window,len(input)):
	available_numbers = input[i - window:i]
	if is_invalid(input[i],available_numbers):
		target_num = input[i]
		target_idx = i

left = 0
right = 1
sum = input[left] + input[right]
while sum != target_num:
	print(input[left:right + 1])
	print(sum)
	if sum < target_num:
		right += 1
		sum += input[right]
	else:
		sum -= input[left]
		left += 1
result = input[left:right + 1]
result.sort()
print("Answer is {}".format(result[0] + result[-1]))
print(datetime.now() - startTime)