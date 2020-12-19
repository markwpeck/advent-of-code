#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def change_direction(cur,lr,deg):
	selector = "ESWN"
	clicks = int(deg / 90)
	curr_idx = selector.index(cur)
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

def move_to_waypoint(position,waypoint,units):
	# print(" - MTW: Position:{}".format(position),end="")
	# print("  Waypoint:{}".format(waypoint),end="")
	# print("  Units: {}".format(units))
	for i in range(units):
		for dir in position.keys():
			position[dir] += waypoint[dir]
	return position

def move_waypoint(waypoint,direction,units):
	waypoint[direction] += units
	return waypoint

def rotate_waypoint(waypoint,lr,deg):
	selector = "ESWN"
	clicks = int(deg/90)
	new_waypoint = {}
	for dir in waypoint.keys():
		curr_idx = selector.index(dir)
		if lr == "R":
			new_idx = (curr_idx + clicks) % len(selector)
		else:
			new_idx = (curr_idx - clicks + 4) % len(selector)
		new_waypoint[selector[new_idx]] = waypoint[dir]
	return new_waypoint

if __name__ == "__main__":
	startTime = datetime.now()
	inputfile = sys.argv[1]
	lines = open(inputfile, "r").readlines()
	selector = "ESWN"
	position = {"E":0,"S":0,"W":0,"N":0}
	waypoint = {"E":10,"S":0,"W":0,"N":1}
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

	position = {"E":0,"S":0,"W":0,"N":0}

	# print("Position:{}".format(position),end="")
	# print("  Waypoint:{}".format(waypoint))

	for line in lines:
		(oper,val) = re.match("^([NSEWRLF])(\d+)$",line.rstrip()).group(1,2)
		if oper in ("L","R"):
			waypoint = rotate_waypoint(waypoint,oper,int(val))
		elif oper == "F":
			position = move_to_waypoint(position,waypoint,int(val))
		else:
			waypoint = move_waypoint(waypoint,oper,int(val))
		# print("Position:{}".format(position),end="")
		# print("  Waypoint:{}".format(waypoint))
	eastwest = abs(position["E"] - position["W"])
	northsouth = abs(position["N"] - position["S"])
	print("Part B: {}".format(eastwest + northsouth))

	print(datetime.now() - startTime)