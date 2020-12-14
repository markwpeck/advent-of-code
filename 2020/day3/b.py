#!/usr/bin/env python3
from datetime import datetime

def run_sim(arb_data,sim_spec):
	trees = 0
	x = 1
	incr = sim_spec[0]
	stride = sim_spec[1]
	print("\nSim: Right {}, down {}".format(incr,stride))
	for line_num in range(len(arb_data)):
		line = arb_data[line_num].rstrip("\n")
		if (stride != 1) and ((line_num + 1) % stride == 0):
			print("  : " + line + "    " + line + "")
		else:
			if x > len(line):
				x = x % len(line)
			print("{:2}: ".format(x),end="")
			if line[x - 1] == "#":
				trees += 1
				print(line[:(x - 1)] + "X" + line[x:] + "    " + line)
			else:
				print(line[:(x - 1)] + "O" + line[x:] + "    " + line)
			x = (x + incr)
	print("Found {} trees.".format(trees))
	return trees

startTime = datetime.now()

sims = [[1,1],[3,1],[5,1],[7,1],[1,2]]
product = 0
input = open("input.txt", "r").readlines()
for sim_spec in sims:
	result = run_sim(input,sim_spec)
	if product == 0:
		product = result
	else:
		product = product * result

print("\nFinal Product: {}".format(product))
print(datetime.now() - startTime)