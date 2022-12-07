""" Class Object Constructor attributes methods() """

class Student:     # Class / design / blueprint
    def __init__(self, name, Id):
        self.name = name    # instance variable or attribute
        self.Id = Id        # instance variable or attribute
        # print("A student objcet created")

    def details(self):          #instance method
        print("Name: ", self.name, "ID: ", self.Id)

#===============================================================================================================

# variable = class_name
s1 = Student("Emil", 32)    # 1st object / instance
s2 = Student("Carol", 22)
s1.Id = 33
# We can't access any property of the design class without object reference.
s1.details()
s2.details()
# print("s1", s1)
# print("s2", s2) 