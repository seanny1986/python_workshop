#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple recursive Fibionacci example to demostrate the principle of recursion.

-- Sean Morrison, 2018
"""

# a recursive example of a function that calculates the nth Fibionacci number.
# This function is inefficient. Can you see why? How could it be improved?
def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

n = 6
print("Fibionacci number {} is {}".format(n, fib(n)))