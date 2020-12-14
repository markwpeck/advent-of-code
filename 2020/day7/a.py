#!/usr/bin/env python3
from datetime import datetime
import re

startTime = datetime.now()

def get_parents(d,name,level):
	# print("({}) Called get_parents for {}".format(level,name))
	ancestry = set()
	if name in d.keys():
		for parent in d[name]:
			ancestry.add(parent)
			ancestry |= get_parents(d,parent,level + 1)
	# print("  Sending back {}".format(ancestry))
	return ancestry

parents = {}
input = open("input.txt", "r").readlines()
for line in input:
	(container,remainder) = line.rstrip().split(" bags contain ")
	contents = re.sub(" bag[s]?", "",re.sub("\.$","",remainder))
	options = re.sub("\d+ ","",contents).split(", ")
	for option in options:
		if option in parents.keys():
			parents[option].append(container)
		else:
			parents[option] = [container]

print("Parent data structure:")
print("{")
for i in parents:
	print("  {}:{}".format(i,parents[i]))
print("}\n")

ancestors = get_parents(parents,"shiny gold",1)

print(ancestors)
print("\nTotal ancestors: {}\n".format(len(ancestors)))
print(datetime.now() - startTime)