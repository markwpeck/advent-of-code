#!/usr/bin/env python3

import sys
from datetime import datetime


if __name__ == "__main__":
	inputfile = sys.argv[1]
	startTime = datetime.now()

	lines = open(inputfile, "r").readlines()
	start = int(lines[0].rstrip())
	routes = sorted(set(lines[1].rstrip().split(",")))
	routes.pop()
	routes = [int(x) for x in routes]

	minutes = 0
	bus = 0
	while bus == 0:
		for route in routes:
			if (start + minutes) % route == 0:
				bus = route
		if bus == 0:
			minutes += 1

	print("Part 1: Bus {}, Minutes since start:{}, Product:{}".format(bus,minutes,bus * minutes))
	print(datetime.now() - startTime)

# This solution for Part 2 was cribbed from https://gist.github.com/hamidazimy/56a8495aea39f79d6de9f372c259f7fe -
# I PROMISE I spent all day studying this problem and trying to wrap my head around the CRT.

	buses = lines[1].rstrip().split(",")
	# buses = ["17","x","13","19"] #first occurs at timestamp 3417.
	# buses = ["67","7","59","61"] #first occurs at timestamp 754018.
	# buses = ["67","x","7","59","61"] #first occurs at timestamp 779210.
	# buses = ["67","7","x","59","61"] #first occurs at timestamp 1261476.
	# buses = ["1789","37","47","1889"] #first occurs at timestamp 1202161486.

	buses = [(int(buses[i]), (int(buses[i]) - i) % int(buses[i]))
	    for i in range(len(buses)) if buses[i] != 'x']

	result = 0
	increment = 1

	for bus in buses:
	    while result % bus[0] != bus[1]:
	        result += increment
	    increment *= bus[0]

	print("Part 2: {}".format(result))

