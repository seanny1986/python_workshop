# -*- coding: utf-8 -*-

"""
Examples of simple functions.
-- Sean Morrison, 2018
"""

# a function that takes a single argument
def x_squared(x):
	return x**2

# a function that takes multiple arguments
def calculate_lift(cl, rho, vel, area):
	lift = cl * 0.5 * rho * vel**2 * area
	return lift

# a function that takes zero arguments
def bark():
    print("woof!")

x = 5
print("Output of function 1: {}".format(x_squared(5)))

cl = 1.2
rho = 1.225
vel = 15
wing_area = 1
print("Lift = ", calculate_lift(cl, rho, vel, wing_area), "N")

bark()