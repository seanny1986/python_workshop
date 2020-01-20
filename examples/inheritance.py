# -*- coding: utf-8 -*-

"""
Some examples demonstrating the concept of inheritance. In this case we have a
generic pet class, and both Cat and Dog inherit from this class. We also give
an example of overriding a parent class method.
-- Sean Morrison, 2018
"""

# parent class Pet
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    # demonstrating that this is the parent class print_name method.
    # we override this method below
    def print_name(self):
        print("This is the parent class")
        print(self.name)
    
    # all pets must eat, so this is common to all child classes.
    def eat(self):
        print(self.name, " nom nom noms")
    
class Dog(Pet):
    def __init__(self, name):
        super(Dog, self).__init__(name, "Dog")
    
    # not all pets bark, only dogs do
    def bark (self):
        print(self.name, " says woof!")
    
    # we override the print_name class of the parent here. This method
    # will take precedence
    def print_name (self):
        print("This is the dog child class.")

class Cat(Pet):
    def __init__(self, name):
        super(Cat, self).__init__(name, "Cat")
    
    # not all pets meow, only cats
    def meow(self):
        print(self.name, " says meow!")
    
    # we override the print_name class of the parent here. This method
    # will take precedence
    def print_name(self):
        print("This is the cat child class")
        
# spike is a dog
spike = Dog("spike")

# fido is not an instance of class dog. Therefore, fido has no bark method
fido = Pet("fido", "Dog")

# luke is a cat
luke = Cat("luke")

# what happens when we call the print_name functions?
spike.print_name()
fido.print_name()
luke.print_name()

spike.bark()            # only dogs bark
luke.meow()             # only cats meow
fido.eat()              # all pets eat
spike.eat()             # all pets eat
luke.eat()              # all pets eat


# a brief example of multiple inheritance
print()
class First: 
	def __init__(self): 
		super(First, self).__init__() 
		print("first") 
        
class Second: 
	def __init__(self): 
		super(Second, self).__init__() 
		print("second") 
        
class Third(First, Second): 
	def __init__(self): 
		super(Third, self).__init__() 
		print("third")

# what do you expect will happen here?
First()
Second()
Third()