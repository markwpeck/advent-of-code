#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def eval_reversed(line):
	if re.match("^\d+$",line):
		return int(line)
	if re.match("^\d+ [+*] \d+$",line):
		return eval(line)
	else:
		if "*" in line:
			(first,second) = line.split(" * ",maxsplit=1)
			return eval_reversed(first) * eval_reversed(second)
		else:
			return eval_traditional(line)

def eval_traditional(line):
	if re.match("^\d+ [+*] \d+$",line):
		return eval(line)
	else:
		tokens = line.split(" ")
		operand2 = int(tokens.pop())
		oper = tokens.pop()
		operand1 = eval_traditional(" ".join(tokens))
		return eval("{} {} {}".format(operand1,oper,operand2))

def eval_possible_parens(line,eval_func):
	if "(" not in line and ")" not in line:
		return eval_func(line)
	if re.match("^\([^()]+\)$",line):
		return eval_func(line[1:-1])
	start_idx = 0
	end_idx = 0
	for i in range(len(line)):
		if line[i] == "(":
			start_idx = i
		elif line[i] == ")":
			end_idx = i
			start = line[:start_idx]
			middle = eval_possible_parens(line[start_idx:end_idx+1],eval_func)
			end = line[end_idx+1:]
			return eval_possible_parens("{}{}{}".format(start,middle,end),eval_func)

if __name__ == "__main__":
	startTime = datetime.now()
	inputfile = sys.argv[1]
	lines = open(inputfile, "r").readlines()
	accumulator1 = 0
	accumulator2 = 0
	for line in lines:
		result1 = eval_possible_parens(line.rstrip(),eval_traditional)
		print("1. {} becomes {}.".format(line.rstrip(),result1))
		accumulator1 += result1
		result2 = eval_possible_parens(line.rstrip(),eval_reversed)
		print("2. {} becomes {}.".format(line.rstrip(),result2))
		accumulator2 += result2
	print("1. Sum is {}".format(accumulator1))
	print("2. Sum is {}".format(accumulator2))
	print(datetime.now() - startTime)

	# Expected results from part 1:
	# 1 + 2 * 3 + 4 * 5 + 6 becomes 71.
	# 1 + (2 * 3) + (4 * (5 + 6)) becomes 51.
	# 2 * 3 + (4 * 5) becomes 26.
	# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
	# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
	# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.
	# Sum is 26457

	# Expected results from part 2:
	# 1 + 2 * 3 + 4 * 5 + 6 becomes 231.
	# 1 + (2 * 3) + (4 * (5 + 6)) becomes 51.
	# 2 * 3 + (4 * 5) becomes 46.
	# 5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
	# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
	# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.
	# Sum is 694173