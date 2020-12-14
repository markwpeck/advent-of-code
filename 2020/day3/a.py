#!/usr/bin/env python3
from datetime import datetime

startTime = datetime.now()

# Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
input = open("input.txt", "r").readlines()
trees = 0
x = 1
for line in input:
	line = line.rstrip("\n")
	if x > len(line):
		x = x % len(line)
	print("{:2}: ".format(x),end="")
	if line[x - 1] == "#":
		trees += 1
		print(line[:(x - 1)] + "X" + line[x:])
	else:
		print(line[:(x - 1)] + "O" + line[x:])
	x = (x + 3)

print("\nEncountered {} trees.".format(trees))
print(datetime.now() - startTime)