#!/usr/bin/env python3
from datetime import datetime

def get_node(node_spec,edges):
	print("> {} {}".format(node_spec,edges))
	if len(node_spec) == 1:
		if node_spec[0] in ("F","L"):
			return edges[0]
		else:
			return edges[1]
	else:
		middle = (edges[1] + edges[0]) // 2
		if node_spec[0] in ("F","L"):
			return get_node(node_spec[1:],(edges[0], middle))
		else:
			return get_node(node_spec[1:],(middle + 1, edges[1]))

startTime = datetime.now()

max_id = 0
input = open("input.txt", "r").readlines()
for line in input:
	line = line.rstrip()
	print(">>> Next Up: {}".format(line))
	row_num = get_node(line[:7],(0,127))
	col_num = get_node(line[7:],(0,7))
	this_id = row_num * 8 + col_num
	print(">>> row {}, column {}, id {}".format(row_num,col_num,this_id))
	if this_id > max_id:
		max_id = this_id
		print("MaxID is now {}".format(max_id))

print("MaxID is {}".format(max_id))
print(datetime.now() - startTime)

# Start by considering the whole range, rows 0 through 127.
# F means to take the lower half, keeping rows 0 through 63.
# B means to take the upper half, keeping rows 32 through 63.
# F means to take the lower half, keeping rows 32 through 47.
# B means to take the upper half, keeping rows 40 through 47.
# B keeps rows 44 through 47.
# F keeps rows 44 through 45.
# The final F keeps the lower of the two, row 44.
