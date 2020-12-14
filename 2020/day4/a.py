#!/usr/bin/env python3
from datetime import datetime
import re

def valid_year(start, end):
	return lambda year: start <= int(year) <= end

def valid_for_units(unit_specs,height):
	match = re.match("^(\d+)(cm|in)",height)
	if match:
		(value_str, units) = match.group(1,2)
		value = int(value_str)
		return unit_specs[units][0] <= value <= unit_specs[units][1]
	else:
		return False

def valid_for_pattern(pattern,value):
	match = re.match(pattern,value)
	if match:
		return match.group(0) == value
	else:
		return False
		
def valid_height(unit_specs):
	return lambda height: valid_for_units(unit_specs, height)

def valid_pattern(pat):
	return lambda val: valid_for_pattern(pat,val)

def valid_in_list(good_values):
	return lambda val: val in good_values

def validate(passport):
	valid_eye_colors = ["amb","blu","brn","gry","grn","hzl","oth"]
	unit_specs = {"cm": [150,193], "in": [59,76]}
	required_fields = {
		"byr": valid_year(1920,2002),
		"iyr": valid_year(2010,2020),
		"eyr": valid_year(2020,2030),
		"hgt": valid_height(unit_specs),
		"hcl": valid_pattern("^#[0-9a-f]{6}$"),
		"ecl": valid_in_list(valid_eye_colors),
		"pid": valid_pattern("\d{9}")
	}
	result = 1
	record_str = " ".join(row.strip() for row in passport)
	print(record_str)
	record = dict([field.split(":") for field in record_str.split()])
	for key in list(required_fields):
		if key not in record:
#			print("-- Couldn't find a {}.".format(key))
			result = 0
		elif required_fields[key](record[key]) is False:
			print("-- Value {} not valid for {}".format(record[key],key))
			result = 0
	return result


startTime = datetime.now()

lines = []
valid = 0
input = open("input.txt", "r").readlines()
for line in input:
	if line.strip() == "":
		if len(lines) > 0:
			valid += validate(lines)
			lines = []
	else:
		lines.append(line)
if len(lines) > 0:
	valid += validate(lines)

print("Found {} valid passports.".format(valid))
print(datetime.now() - startTime)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.