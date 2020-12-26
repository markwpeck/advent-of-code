#!/usr/bin/env python3
import sys
import re
from tile import Tile
from datetime import datetime

def read_file(inputfile):
	tile_d = dict()
	tile_id = 0
	tile_ary = []
	lines = open(inputfile, "r").readlines()
	for line in lines:
		match = re.match("^Tile (\d+):$",line)
		if match:
			tile_id = int(match.group(1))
		elif line.rstrip() == "":
			tile_d[tile_id] = Tile(tile_id,tile_ary)
			tile_ary.clear()
		else:
			tile_ary.append(line.rstrip())
	return tile_d

def main():
	inputfile = sys.argv[1]
	startTime = datetime.now()
	tiles = read_file(inputfile)

	unchecked_tiles = list(tiles.values())
	corners = set()

	for tile in unchecked_tiles:
		if tile.neighbors == 4:
			print("{} already has four neighbors, skipping.".format(tile.id))
			continue
		for other_tile in unchecked_tiles:
			if tile.id == other_tile.id:
				continue
			# if other_tile.neighbors == 4:
			# 	continue
			intersection = tile.permutations.intersection(other_tile.permutations)
			if intersection:
				print("{} has {} common sides with {}".format(tile.id,len(intersection),other_tile.id))
				print(intersection)
				tile.neighbors += 1
				other_tile.neighbors += 1
		print("{} has {} neighbors".format(tile.id,tile.neighbors))
		if tile.neighbors == 2:
			corners.add(tile)

	# tile = tiles[1951]
	# print(tile)
	# print(tile.permutations)

	product = 1
	for tile in corners:
		print(tile)
		product *= tile.id

	print(datetime.now() - startTime)

if __name__ == "__main__":
	main()
