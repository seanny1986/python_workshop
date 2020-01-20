# -*- coding: utf-8 -*-
"""
Simple class example. Within the class dog, there are multiple functions that
belong to an instance of class dog. Every instance of class dog will have these
functions, but the values saved to the class variables will be different.
-- Sean Morrison
"""

# since we can have multiple instances of the same class, each instance has to
# also refer to itself. Variables prefixed with "self" belong to the class.
# the __init__ function is a special function that needs to be included whenever
# you write a new class.
class Dog:
    def __init__(self, name, breed, height, weight, age):
        self.name = name
        self.breed = breed
        self.height = height
        self.weight = weight
        self.age = age

    def bark(self):
        print(self.name, "says woof!")
        
    def get_name(self):
        return self.name
            
    def get_age(self):
        return self.age
    
    def get_breed(self):
        return self.breed

fido = Dog("fido", "labrador", 0.45, 30, 7)
fido.bark()
print(fido.get_name(), "is a ", fido.get_breed())
print(fido.get_name(), " is ", fido.get_age(), "years old")

spike = Dog("spike", "pit bull", 0.4, 30, 6)
print(spike.get_name(), "is a ", spike.get_breed())
print(spike.get_name(), " is ", spike.get_age(), "years old")