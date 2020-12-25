#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def build_ruleset(rule):
	result = []
	options = rule.split("|")
	for opt_idx in range(len(options)):
		sequence = options[opt_idx].strip().split(" ")
		result.append(sequence)
	return result

def get_regex(rulesets,idx,depth):
	result = ""
	ruleset = rulesets[idx]
	if ruleset[0][0] in ['"a"','"b"']:
		result = ruleset[0][0][1]
	else:
		options = []
		for option in ruleset:
			opt_str = ""
			for item in option:
				if item in ["8","11"] and part == "b" and int(item) == idx:
					if depth <= 7:
						print("Index {} ({}): Hit item {}".format(idx,depth,item))
						opt_str += get_regex(rulesets,int(item),depth + 1)
				else:
					opt_str += get_regex(rulesets,int(item),depth)
			options.append(opt_str)
		result = "(" + "|".join(options) + ")"
	return result	

if __name__ == "__main__":
	inputfile = sys.argv[1]
	startTime = datetime.now()
	rulesets = {}
	messages = []
	lines = open(inputfile, "r").readlines()
	part = input("Part a or part b? ")
	section = "rules"
	for line in lines:
		line = line.rstrip()
		if line == "":
			section = "messages"
			continue
		if section == "rules":
			(index,rule) = line.split(":")
			if index == "8" and part == "b":
				rule = "42 | 42 8"
			elif index == "11" and part == "b":
				rule = "42 31 | 42 11 31"
			rulesets[int(index)] = build_ruleset(rule.strip())
		else:
			messages.append(line)

	# print("Rulesets:")
	# for rs_idx in sorted(rulesets.keys()):
	# 	print("{:3}:".format(rs_idx))
	# 	for option in rulesets[rs_idx]:
	# 		print("  {}".format(option))

	matches = 0

	pattern = get_regex(rulesets,0,0)
	# print("Regex Pattern:{}".format(pattern))
	# print("Length:{}".format(len(pattern)))
	rule0 = re.compile(pattern)

	for message in messages:
		if rule0.fullmatch(message):
			matches += 1
		# 	print("  ({:3}) {} is a valid message.".format(len(message),message))
		else:
			print("  ({:3}) {} is NOT a valid message.".format(len(message),message))

	print("Total Messages:{}".format(len(messages)))
	print("Matches:{}".format(matches))
	print(datetime.now() - startTime)