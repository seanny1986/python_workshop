# -*- coding: utf-8 -*-

"""
Playing with some variables
-- Sean Morrison, 2018
"""

x = "Hello, "
y = "my name is Boris."
z = x+y
print(z)
k = z.split(",")
print(k)
print(k[-1])

a = 5
b = 10.3
print("a = ", a)
print(type(a))
print("b = ", b)
print(type(b))

A = []
A.append(a)
A.append(b)
A.append(z)
print("Contents of list A are:")
print(A)
print("Length of list A is ", len(A))

y = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
b = y[0][:]
print(b)
