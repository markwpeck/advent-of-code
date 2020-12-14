#!/usr/bin/env python3

exprpt = open("expensereport.txt", "r")
expenses = exprpt.readlines()
while(len(expenses) > 0):
	a = int(expenses.pop())
	for bstr in expenses:
		b = int(bstr)
		for cstr in expenses:
			c = int(cstr)
			if (a + b + c) == 2020:
				print('a is {}, b is {}, c is {}, sum is {}, product is {}'.format(a,b,c,a + b + c,a * b * c))