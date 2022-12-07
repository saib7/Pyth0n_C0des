# class method -1
class Student:

    uni_name = "BRACU" # class variable / attribute

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):   # instance method
        print("Name:", self.name, "ID:", self.__id, Student.uni_name)
        

    # def up_uni_name(self, u_name):
    #     self.uni_name = u_name 
    
    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name 

#===================================================================================================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)

s1.details()
s2.details()

# s1.up_uni_name("BRAC University")
Student.up_uni_name("BRAC University")

s1.details()
s2.details()

print(s1.__dict__)