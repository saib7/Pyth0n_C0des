# Inheritance (Hierarchical inheritance)
class Student:

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):   # instance method
        print("Name:", self.name, "ID:", self.__id)

#===========================================================================================================================
class CSEstudent(Student):
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of", self.no_of_labs)

#===========================================================================================================================
class BBAstudent(Student):
    
    def __init__(self, name, Id):
        super().__init__(name, Id)

    def party(self):
        print("All day party.")
 
#===========================================================================================================================

s1 = CSEstudent("Bob", 11, 3)
s2 = BBAstudent("Carol", 36)

print(s1.__dict__)
s1.details()
s2.details()

s1.cry()
s2.party()
# print(help(s1))
