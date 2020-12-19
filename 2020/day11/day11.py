#!/usr/bin/env python3
import sys
from datetime import datetime

def how_many_occupied(room):
	occupied = 0
	for row in room:
		for chair in row:
			if chair == "#":
				occupied += 1
	return occupied

# def line_of_sight(room,i,j):
# 	crowding = {}
# 	for row in range(len(room)):
# 		for col in range(len(room[row])):
# 			if room[row][col] == "#":


def adjacent(room,i,j):
	crowding = 0
	for row in range(max(0,i-1),min(i+2,len(room))):
		# print("{},{} - row:{}".format(i,j,row))
		for col in range(max(0,j-1),min(j+2,len(room[i]))):
			# print("{},{} - col:{}".format(i,j,col))
			if room[row][col] == "#":
				if row in (i-1,i,i+1) and abs(col-j) == 1:
					crowding += 1
				elif col == j and abs(row-i) == 1:
					crowding += 1
	return crowding

def recalc(room,calc_method,crowding_limit):
	new_room = []
	for i in range(len(room)):
		new_row = []
		for j in range(len(room[i])):
			crowding = calc_method(room,i,j)
			# print("{} chairs occupied around me.".format(crowding))
			if room[i][j] == "L" and crowding == 0:
				new_row.append("#")
			elif room[i][j] == "#" and crowding >= crowding_limit:
				new_row.append("L")
			else:
				new_row.append(room[i][j])
		new_room.append(new_row)
	return new_room

def print_compare(old_room,new_room):
	print("\nOld Room:     New Room:")
	for row in range(len(old_room)):
		old_row = "".join(char for char in old_room[row])
		new_row = "".join(char for char in new_room[row])
		print("{}    {}".format(old_row,new_row))

if __name__ == "__main__":
	inputfile = sys.argv[1]
	lines = open(inputfile, "r").readlines()

	startTime = datetime.now()
	room = []
	for i in range (len(lines)):
		room.append([char for char in lines[i].rstrip()])

	while True:
		new_room = recalc(room,adjacent,4)
		# print_compare(room,new_room)
		if how_many_occupied(new_room) == how_many_occupied(room):
			break
		room = new_room

	print("Part A: {}".format(how_many_occupied(room)))
	print(datetime.now() - startTime)

	# startTime = datetime.now()
	# room = []
	# for i in range (len(lines)):
	# 	room.append([char for char in lines[i].rstrip()])

	# while True:
	# 	new_room = recalc(room,line_of_sight,5)
	# 	# print_compare(room,new_room)
	# 	if how_many_occupied(new_room) == how_many_occupied(room):
	# 		break
	# 	room = new_room

	# print("Part B: {}".format(how_many_occupied(room)))

	# print(datetime.now() - startTime)