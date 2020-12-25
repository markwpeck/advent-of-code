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
				opt_str += get_regex(rulesets,int(item),depth + 1)
			options.append(opt_str)
		result = "(" + "|".join(options) + ")"
	return result	

if __name__ == "__main__":
	inputfile = sys.argv[1]
	startTime = datetime.now()
	rulesets = {}
	messages = []
	lines = open(inputfile, "r").readlines()
	section = "rules"
	for line in lines:
		line = line.rstrip()
		if line == "":
			section = "messages"
			continue
		if section == "rules":
			(index,rule) = line.split(":")
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
	print("Regex Pattern:{}".format(pattern))
	rule0 = re.compile(pattern)

	for message in messages:
		if rule0.fullmatch(message):
			matches += 1

	print("Total Messages:{}".format(len(messages)))
	print("Matches:{}".format(matches))
	print(datetime.now() - startTime)