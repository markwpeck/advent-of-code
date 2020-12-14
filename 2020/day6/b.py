#!/usr/bin/env python3
from datetime import datetime
import string

def count_answers(lines):
	d = dict.fromkeys(string.ascii_lowercase, 0)
	members = len(lines)
	result = 0
	record_str = "".join(row.strip() for row in lines)
	for letter in record_str:
		d[letter] += 1
	for i in d.keys():
		if d[i] == members:
			result += 1
	return result

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