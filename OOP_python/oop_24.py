# Inheritance (Multilevel inheritance)
class Student:      # grand parent class

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):   # instance method
        print("Name:", self.name, "ID:", self.__id)

#===========================================================================================================================
class CSEstudent(Student):    # parent class
    def __init__(self, name, Id, labs):
        super().__init__(name, Id)
        self.no_of_labs = labs

    def cry(self):
        print("CSE student is crying because of", self.no_of_labs, "lab(s)")

#===========================================================================================================================
class CSEfresher(CSEstudent):   # child class

    def enroll_cse110(self):
        print(self.name, "Enrolled in CSE110.")
#===========================================================================================================================

s1 = CSEstudent("Bob", 11, 3)
s2 = CSEfresher("Carol", 55, 1)

s2.details()
s1.details()
s1.cry()
s2.cry()
s2.enroll_cse110()

# s1.enroll_cse110() # won't work
