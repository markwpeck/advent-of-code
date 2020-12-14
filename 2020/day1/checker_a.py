#!/usr/bin/env python3

exprpt = open("expensereport.txt", "r")
expenses = exprpt.readlines()
while(len(expenses) > 0):
	a = int(expenses.pop())
	for bstr in expenses:
		b = int(bstr)
		if (a + b) == 2020:
			print('a is {}, b is {}, sum is {}, product is {}'.format(a,b,a + b,a * b))