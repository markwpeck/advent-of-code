#!/usr/bin/env python3
from datetime import datetime
import re

startTime = datetime.now()

def get_required(d,name,level):
	# print("{}({}) Called get_required for {}".format(" " * level,level,name))
	required = 0
	if name in d.keys():
		for bag_type in d[name].keys():
			required += (get_required(d,bag_type,level + 1) + 1) * d[name][bag_type]
	# print("{}({}) Sending back {}".format(" " * level, level, required))
	return required

children = {}
input = open("input.txt", "r").readlines()
for line in input:
	(container,remainder) = line.rstrip().split(" bags contain ")
	contents = re.sub(" bag[s]?", "",re.sub("\.$","",remainder))
	options = contents.split(", ")
	children[container] = {}
	for option in options:
		match = re.match("^(\d+) (\w+ \w+)$",option)
		if match:
			(quantity,name) = match.group(1,2)
			children[container][name] = int(quantity)
		else:
			children.pop(container)

# print("Children data structure:")
# print("{")
# for bag in children.keys():
# 	print("  {} ->".format(bag))
# 	for child in children[bag].keys():
# 		print("    {}:{}".format(child,children[bag][child]))
# print("}\n")

must_haves = get_required(children,"shiny gold",1)

print("\nTotal bags required: {}\n".format(must_haves))
print(datetime.now() - startTime)