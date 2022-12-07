class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def update_color(self, color):
        self.color = color

    def poke(self):
        print(self.color, self.name, "is smiling.")


#================================================================================================================

d1 = Dog("Akila", "White")
d2 = Dog("Ghost", "Brown")

d1.poke()
d1.update_color("Black")
d1.poke()
d2.poke()
d2.update_color("Red")
d2.poke()

print(d1.__dict__) # __dict__ helps to check the value of object's attribute as a dictionary.
print(d2.__dict__) # __dict__ helps to check the value of object's attribute as a dictionary.

print(dir(d1)) # helps to print all methods and attributes of the object as a list
