# -*- coding: utf-8 -*-

"""
Example of single and nested lambda functions.
-- Sean Morrison, 2018
"""

from math import sqrt

f = lambda x: x**2
y = 5
print("Output of f(y) is {}".format(f(y)))

g = lambda x: (lambda y: sqrt(y))(x**2)
z = 2
print("Output of g(z) is {}".format(g(z)))