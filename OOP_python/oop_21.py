#static method
class Student:

    uni_name = "BRACU" # class variable / attribute

    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):   # instance method
        print("Name:", self.name, "ID:", self.__id, Student.uni_name)
    
    @classmethod
    def up_uni_name(cls, u_name):
        cls.uni_name = u_name 

    @staticmethod                         # static method , aka utility function
    def check_department(Id):
        if Id[3:5] == "01":
            print("CSE")
        elif Id[3:5] == "41":
            print("CS")


#==============================================================================================================================
Student.check_department("14341006")  # static method doesn't depends on instance creation
s1 = Student("Bob", 11)
s2 = Student("Carol", 47)

s1.details()
s2.details()

Student.check_department("15301007")

