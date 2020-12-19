#!/usr/bin/env python3
from datetime import datetime

startTime = datetime.now()
# iterTime = datetime.now()

def get_hash(s):
	return " ".join([str(i) for i in s])

def check_for_removals(aset,solution_d):
	# global iterTime
	hashkey = get_hash(aset)
	if hashkey in solution_d.keys():
		return (solution_d)
	# print(hashkey)
	solution_d[hashkey] = True
	if len(solution_d.keys()) % 10000 == 0:
		print("Solution dictionary has {:,} keys.".format(len(solution_d.keys())))
		# print(datetime.now() - iterTime)
		print(datetime.now() - startTime)
		# iterTime = datetime.now()
	for i in range(1,len(aset) - 1):
		if 0 <= (aset[i + 1] - aset[i - 1]) <= 3:
			cset = aset[:]
			del cset[i]
			solution_d = check_for_removals(cset,solution_d)
	return solution_d

raw_input = open("input.txt", "r").readlines()
input = [int(x) for x in raw_input]
input.sort()
input.insert(0,0)
input.append(input[-1] + 3)
solutions = {}

solutions = check_for_removals(input,solutions)

print(len(solutions.keys()))

print("Total run time:")
print(datetime.now() - startTime)