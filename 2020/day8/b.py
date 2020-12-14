#!/usr/bin/env python3
from datetime import datetime
import re

def display_instruction(pc,acc,instruction,value):
	print("({:4}) {} {:4} | acc:{:6}".format(pc,instruction,value,acc))

def execute_instruction(program,pc,acc):
	next_incr = 1
	(instruction, value) = program[pc].rstrip().split(" ")
	if instruction == "acc":
		acc += int(value)
		next_incr = 1
	elif instruction == "jmp":
		next_incr = int(value)
	else:
		next_incr = 1
	display_instruction(pc,acc,instruction,value)
	pc += next_incr
	return (pc, acc)

def get_new_program(original_program,last_modified_line):
	made_change = False
	new_program = []
	for i in range(len(original_program)):
		line = original_program[i]
		if made_change or i <= last_modified_line:
			new_program.append(line)
		elif "nop" in line:
			print("  Original instruction: {}".format(line.rstrip()))
			new_line = line.replace("nop","jmp")
			print("  Replaced instruction: {}".format(new_line.rstrip()))
			new_program.append(new_line)
			last_modified_line = i
			made_change = True
		elif "jmp" in line:
			print("  Original instruction: {}".format(line.rstrip()))
			new_line = line.replace("jmp","nop")
			print("  Replaced instruction: {}".format(new_line.rstrip()))
			new_program.append(new_line)
			last_modified_line = i
			made_change = True
		else:
			new_program.append(line)
	print("  I changed line {} this time".format(last_modified_line))
	return (new_program,last_modified_line)


def run_program(program):
	pc = 0
	acc = 0
	visited = []
	for i in range(len(program)):
		visited.append(False)
	while True:
		visited[pc] = True
		(pc, acc) = execute_instruction(program,pc,acc)
		# print("pc is {}, program is {} lines long".format(pc,len(program)))
		if pc >= len(program):
			break
		if visited[pc] == True:
			print("ERMEGERSH! I've been here before. Stopping.")
			return (pc, acc)
	return (pc,acc)


startTime = datetime.now()
original_program = open("input.txt", "r").readlines()
last_modified_line = -1
while True:
	(new_program,last_modified_line) = get_new_program(original_program,last_modified_line)
	(exit_pc,exit_acc) = run_program(new_program)
	if exit_pc >= len(new_program):
		print("Success! ACC is {}".format(exit_acc))
		break
	else:
		print("Argh, that didn't work. ACC is {}".format(exit_acc))

print(datetime.now() - startTime)