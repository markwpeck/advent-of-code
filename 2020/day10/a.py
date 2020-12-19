#!/usr/bin/env python3
from datetime import datetime

startTime = datetime.now()

gap_counts = {1:0,2:0,3:0}
raw_input = open("input.txt", "r").readlines()
input = [int(x) for x in raw_input]
input.sort()
input.insert(0,0)
input.append(input[-1] + 3)
while(len(input) > 1):
	print(input)
	last = input.pop()
	gap_counts[last - input[-1]] += 1
print(gap_counts)
print(gap_counts[1] * gap_counts[3])
print(datetime.now() - startTime)