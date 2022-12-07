# Inheritance (single inheritance)
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

#====================================================================================================================================
class Dog(Animal):
    
    def bark(self):
        print(self.name, "is barking.")

#====================================================================================================================================

a1 = Animal("Jack")
d1 = Dog("Rover")
# d1.bark()
# d1.eat()
# a1.eat()
# a1.bark()

#isinstance(Object, ClassName)
print(isinstance(d1, Animal))
print(isinstance(d1, Dog))
print(isinstance(a1,Animal))
print(isinstance(a1, Dog))

print("--000--")

#issubclass(Class, ClassName)
print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
