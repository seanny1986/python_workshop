# -*- coding: utf-8 -*-

"""
Playing around with some basic math operations.

-- Sean Morrison, 2018
"""

from math import sin, cos, sqrt, pi

x = sin(pi)+3*cos(pi)+tan(pi)-sqrt(2)
print("x = ", x)

y = 5**2-7
print("y = ", y)

z = (x+1)*5/3-7+y
print("z = ", z)

"""
And some logical operations

-- Sean Morrison
"""

a = 1>0
b = not a
c = type(a) is str

print(a)
print(b)
print(c)