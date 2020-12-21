#!/usr/bin/env python3
import sys
from datetime import datetime



if __name__ == "__main__":
	startTime = datetime.now()
	inputarg = sys.argv[1]
	seed = []
	if "example" in inputarg:
		seed = [0,3,6]
		# seed = [3,1,2]
	else:
		seed = [0,13,1,16,6,17]
	seed.reverse()
	transcript = []
	history = {}
	first = {}
	for turn in range(30000000):
		if len(seed) > 0:
			spoken_number = seed.pop()
		else:
			previous_number = transcript[-1]
			if first[previous_number] == turn - 1:
				spoken_number = 0
			else:
				spoken_number = history[previous_number][-1] - history[previous_number][-2]
		if spoken_number not in first:
			first[spoken_number] = turn
			history[spoken_number] = []
		transcript.append(spoken_number)
		history[spoken_number].append(turn)
	print(transcript[-1])
	print(datetime.now() - startTime)