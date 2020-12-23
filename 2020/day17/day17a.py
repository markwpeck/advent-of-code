#!/usr/bin/env python3
import sys
from datetime import datetime

def get_initial_state(inputfile):
	pocket = {}
	lines = open(inputfile, "r").readlines()
	midi = int(len(lines) / 2)
	for y in range(len(lines)):
		yline = lines[y]
		for x in range(len(lines)):
			if yline[x] == "#":
				coord = (x-midi,midi-y,0)
				pocket[coord] = get_neighbors(coord)
	return pocket

def get_neighbors(coordinates):
	(mx,my,mz) = coordinates
	neighbors = set()
	for x in [mx-1,mx,mx+1]:
		for y in [my-1,my,my+1]:
			for z in [mz-1,mz,mz+1]:
				new_coord = (x,y,z)
				if new_coord != coordinates:
					neighbors.add(new_coord)
	return neighbors

def print_pocket(pocket):
	maxvals = list(map(max,zip(*pocket)))
	minvals = list(map(min,zip(*pocket)))
	for z in range(minvals[2],maxvals[2]+1):
		print("\nz={}".format(z))
		for y in range(maxvals[1],minvals[1]-1,-1):
			result = ""
			for x in range(minvals[0],maxvals[0]+1):
				if (x,y,z) in pocket:
					result += "#"
				else:
					result += "."
			print(result)

def cycle_pocket(pocket):
	new_pocket = {}
	for coord in pocket.keys():
		neighbors = pocket[coord]
		if get_next_state(coord,pocket,neighbors) == "Active":
			new_pocket[coord] = neighbors
		for neighbor in neighbors:
			his_neighbors = get_neighbors(neighbor)
			if get_next_state(neighbor,pocket,his_neighbors) == "Active":
				new_pocket[neighbor] = his_neighbors
	return new_pocket

def get_next_state(coord,pocket,neighbors):
	active_neighbors = 0
	for neighbor in neighbors:
		if neighbor in pocket:
			active_neighbors += 1
	if coord in pocket and active_neighbors in [2,3]:
		return "Active"
	if coord not in pocket and active_neighbors == 3:
		return "Active"
	return "Inactive"

if __name__ == "__main__":
	inputfile = sys.argv[1]
	# startTime = datetime.now()

	pocket = get_initial_state(inputfile)
	print("Before any cycles:")
	print_pocket(pocket)
	for i in range(1,7):
		pocket = cycle_pocket(pocket)
		print("After {} {}:".format(i,"cycle" if i == 1 else "cycles"))
		print_pocket(pocket)

	print("Active nodes: {}".format(len(pocket)))
	# print(datetime.now() - startTime)