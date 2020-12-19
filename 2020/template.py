#!/usr/bin/env python3
import sys
from datetime import datetime



if __name__ == "__main__":
	inputfile = sys.argv[1]
	lines = open("input.txt", "r").readlines()
	startTime = datetime.now()
	print(datetime.now() - startTime)