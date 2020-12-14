#!/usr/bin/env python3
from datetime import datetime

def count_answers(lines):
	results = {}
	record_str = "".join(row.strip() for row in lines)
	for letter in record_str:
		results[letter] = True
	print("({}) ".format(len(results)) + record_str)
	return len(results)

startTime = datetime.now()

input = open("input.txt", "r").readlines()

lines = []
total_counts = 0

for line in input:
	if line.strip() == "":
		if len(lines) > 0:
			total_counts += count_answers(lines)
			lines = []
	else:
		lines.append(line)
if len(lines) > 0:
	total_counts += count_answers(lines)

print("Sum is {}".format(total_counts))
print(datetime.now() - startTime)