# Abstract class and method --3

from abc import ABC, abstractclassmethod

class Animal(ABC): # an abstract class can have both concrete and abstract methods # Abstract class
    @abstractclassmethod
    def make_sound(self): # abstract method , it should not have a body
        pass
    
    def eat(self):
        print("I am eating.")

#======================================================================================================================================
class Dog(Animal):
    def make_sound(self):
        print("Dog barking.")
#======================================================================================================================================
class Cat(Animal):  
    def make_sound(self):  
        print("Meow Meow.")
#======================================================================================================================================
class Snake(Animal):
    def make_sound(self):
        print("Hiss Hiss.")

d1 = Dog()
d1.make_sound()
d1.eat()

c1 = Cat()
c1.make_sound()
c1.eat()

s1 = Snake()
s1.make_sound()
