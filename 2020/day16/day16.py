#!/usr/bin/env python3
import sys
from datetime import datetime
import re

field_spec = "^([a-z]+):(\d+)-(\d+)or(\d+)-(\d+)$"

def get_field_positions(field_possibilities):
	field_positions = []
	return field_positions

def get_field_possibilities(field_values,valid_tickets):
	field_possibilities = {}
	for i in range(len(field_values)):
		field_possibilities[i] = set()
		ticket_values = [ticket[i] for ticket in valid_tickets]
		for field_name in field_values.keys():
			field_is_valid = True
			for value in ticket_values:
				if value not in field_values[field_name]:
					field_is_valid = False
			if field_is_valid == True:
				field_possibilities[i].add(field_name)
	return field_possibilities

def readfile(lines):
	section = "fieldspecs"
	field_values = {}
	all_fields = set()
	valid_tickets = []
	p1_error_rate = 0
	for line in lines:
		line = line.replace(" ","")
		if line.rstrip() == "":
			continue
		if line.rstrip() == "yourticket:":
			section = "yourticket"
			continue
		if line.rstrip() == "nearbytickets:":
			section = "nearbytickets"
			continue
		if (section == "fieldspecs"):
			match = re.match(field_spec,line.rstrip())
			field_name = match.group(1)
			field_values[field_name] = set()
			range1 = range(int(match.group(2)),int(match.group(3)) + 1)
			field_values[field_name].update(range1)
			all_fields.update(range1)
			range2 = range(int(match.group(4)),int(match.group(5)) + 1):
			field_values[field_name].update(range2)
			all_fields.update(range2)
		elif (section == "yourticket"):
			yourticket = [int(x) for x in line.rstrip().split(",")]
		elif (section == "nearbytickets"):
			ticket = [int(x) for x in line.rstrip().split(",")]
			ticket_is_valid = True
			for field in ticket:
				if field not in all_fields:
					p1_error_rate += field
					ticket_is_valid = False
			if ticket_is_valid:
				valid_tickets.append(ticket)
	print("P1 Error Rate:{}".format(p1_error_rate))
	return (field_values,all_fields,valid_tickets,yourticket)


if __name__ == "__main__":
	startTime = datetime.now()
	inputfile = sys.argv[1]
	(field_values,all_fields,valid_tickets,yourticket) = readfile(open(inputfile, "r").readlines())
	field_possibilities = get_field_possibilities(field_values,valid_tickets)
	field_positions = get_field_positions(field_possibilities)
	# print("Field Positions:")
	# for p in range(len(field_positions)):
	# 	print("{}: {}".format(p,field_positions[p]))

	# result = 1
	# for i in range(len(yourticket)):
	# 	if "departure" in field_positions[i]:
	# 		result *= yourticket[i]
	# print("P2 Answer:{}".format(result))
	print(datetime.now() - startTime)