#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def change_direction(cur,lr,deg):
	selector = "ESWN"
	curr_idx = selector.index(cur)
	clicks = int(deg / 90)
	if lr == "R":
		new_idx = (curr_idx + clicks) % len(selector)
	else:
		new_idx = (curr_idx - clicks + 4) % len(selector)
	return selector[new_idx]

def change_position(curr_pos,direction,units):
	result = {}
	for dir in curr_pos.keys():
		result[dir] = curr_pos[dir]
	result[direction] += units
	return result

if __name__ == "__main__":
	startTime = datetime.now()
	inputfile = sys.argv[1]
	lines = open(inputfile, "r").readlines()
	selector = "ESWN"
	position = {"E":0,"S":0,"W":0,"N":0}
	navigation = []
	direction = "E"
	for line in lines:
		(oper,val) = re.match("^([NSEWRLF])(\d+)$",line.rstrip()).group(1,2)
		if oper in ("L","R"):
			direction = change_direction(direction,oper,int(val))
		elif oper == "F":
			position = change_position(position,direction,int(val))
		else:
			position = change_position(position,oper,int(val))
	eastwest = abs(position["E"] - position["W"])
	northsouth = abs(position["N"] - position["S"])
	print("Part A: {}".format(eastwest + northsouth))
	print(datetime.now() - startTime)