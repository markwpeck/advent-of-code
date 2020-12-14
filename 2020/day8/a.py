#!/usr/bin/env python3
from datetime import datetime
import re

def display_instruction(instruction, value):
	global pc, acc
	print("({:4}) {} {:4} | acc:{:6}".format(pc,instruction,value,acc))

def execute_program():
	global program, pc, acc, visited
	next_incr = 1
	(instruction, value) = program[pc].rstrip().split(" ")
	if visited[pc] == True:
		print("ERMEGERSH! I've been here before. Stopping.")
		return False
	if instruction == "acc":
		acc += int(value)
		next_incr = 1
	elif instruction == "jmp":
		next_incr = int(value)
	else:
		next_incr = 1
	display_instruction(instruction,  value)
	visited[pc] = True
	pc += next_incr
	return True

startTime = datetime.now()
program = open("input.txt", "r").readlines()
pc = 0
acc = 0
visited = []
for i in range(len(program)):
	visited.append(False)
valid_state = True
while valid_state:
	valid_state = execute_program()
print(datetime.now() - startTime)