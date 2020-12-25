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

def get_valid_messages(rulesets,idx):
	result = set()
	ruleset = rulesets[idx]
	for sequence in ruleset:
		my_seq = sequence.copy()
		strings = set()
		for item in my_seq:
			if item.isdecimal():
				endings = get_valid_messages(rulesets,int(item))
			else:
				endings = set(re.match('^"([a-z])"$',item).group(1))
			if not strings:
				strings = endings
			else:
				new_strings = set()
				for string in strings:
					for ending in endings:
						new_strings.add(string + ending)
				strings = new_strings
		result |= strings
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
	valid_messages = get_valid_messages(rulesets,0)
	print("Valid Messages:")
	for vm in valid_messages:
		if len(vm) != 24:
			print("  {}".format(vm))

	for message in messages:
		if message in valid_messages:
			matches += 1

	print("Total Messages:{}".format(len(messages)))
	print("Total valid messages:{}".format(len(valid_messages)))
	print("Matches:{}".format(matches))
	print(datetime.now() - startTime)