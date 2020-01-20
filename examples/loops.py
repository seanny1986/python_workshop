# -*- coding: utf-8 -*-

"""
Some examples of loops.
-- Sean Morrison, 2018
"""

# looping forward using a for loop. For loops will terminate after a given
# number of iterations.
print("looping using a for loop")
y = 0
print("y = ", y)
for x in range(1, 101):
	y += x 
print("y = ", y)

# looping using a while loop. While loops will continue forever unless
# you provide a terminal condition
print()
print("looping with a while loop. Notice that we have to include a termination condition")
running = True
n = 100
while running:
	y -= n
	n -= 1
	if n == 0:
		break
print("y = ", y)

# iterating through a list
print()
print("iterating through a list")
numbers = [1, 2, 3]
for x in numbers:
	print(x)

# and the same again in reversed order
print()
print("...and the same again in reversed order")
for x in reversed(numbers):
    	print(x)

# another way of doing reversed iterations
print()
print("another way of doing reversed iterations")
for x in numbers[::-1]:
    	print(x)        

print()
print("enumeration of a list")
numbers = [5, 4, 3, 2, 1]
for i, x in enumerate(numbers):
	print("i: {}, x: {}".format(i, x))

print()
print("zipping multiple lists of the same size")
list_1, list_2 = [5, 4, 3, 2, 1], [10, 9, 8, 7, 6]
for x, y in zip(list_1, list_2):
	print("x: {}, y: {}".format(x, y)) 
    
print()
print("list comprehension example")
a = [x for x in range(5)]
print(a)

print()
print("nested list comprehension example")
b = [[x+y for x in range(3)] for y in range(3)]
print(b)