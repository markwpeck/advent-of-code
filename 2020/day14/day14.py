#!/usr/bin/env python3
import sys
import re
from datetime import datetime

def get_masked_value(mask,val):  # Part 1 function
	setmask = int(mask.replace("X","0"),2)
	val |= setmask
	clearmask = int(mask.replace("X","1"),2)
	val &= clearmask
	return val

def get_addresses(addr_int,mask):  # Part 2 function
	setmask = int(mask.replace("X","0"),2)
	addr_int |= setmask
	addr_str = "{0:b}".format(addr_int).zfill(36)
	for i in range(len(mask)):
		if mask[i] == "X":
			addr_str = addr_str[:i] + "X" + addr_str[i+1:]
	addresses = float_explode("",addr_str)
	return addresses

def float_explode(seed,address_spec):  # Part 2 function
	address_list = []
	if len(seed) == len(address_spec):
		address_list.append(seed)
	else:
		idx = len(seed)
		if address_spec[idx] == "X":
			address_list.extend(float_explode(seed + "1", address_spec))
			address_list.extend(float_explode(seed + "0", address_spec))
		else:
			address_list.extend(float_explode(seed + address_spec[idx], address_spec))
	return address_list

if __name__ == "__main__":
	inputfile = sys.argv[1]
	lines = open(inputfile, "r").readlines()
	startTime = datetime.now()
	addresses = {}
	mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
	for line in lines:
		if "mem" in line:
			(addr,val) = re.match("^mem\[(\d+)\] = (\d+)",line).group(1,2)
			addresses[int(addr)] = get_masked_value(mask,int(val))
		else:
			mask = re.match("^mask = ([X10]{36})$",line).group(1)

	total = 0
	for key in addresses.keys():
		total += addresses[key]

	print("Part 1: Sum is {}".format(total))
	print(datetime.now() - startTime)

	addresses = {}
	mask = "000000000000000000000000000000000000"
	for line in lines:
		if "mem" in line:
			(addr,val) = re.match("^mem\[(\d+)\] = (\d+)",line).group(1,2)
			for addr in get_addresses(int(addr),mask):
				addresses[int(addr)] = int(val)
		else:
			mask = re.match("^mask = ([X10]{36})$",line).group(1)

	total = 0
	for key in addresses.keys():
		total += addresses[key]

	print("Part 2: Sum is {}".format(total))
	print(datetime.now() - startTime)