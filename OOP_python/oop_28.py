# The __str__() method

class Student:
    def __init__(self, name, Id):
        self.name = name
        self.id = Id
        # print(self)

    def __str__(self): # __str__() method must return string (& don't print)
        return "This is " + str(self.name)

#=====================================================================================================================================
s1 = Student("Bob", 11)
s2 = Student("Carol", 11)

print(s1)
print(s1.__str__()) # When we try to call or instantiate any object, we by default call this method(.__str__())

print(s2)