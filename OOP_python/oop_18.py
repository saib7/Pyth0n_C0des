# Class or Static Variable (ex-2)
class Student:
    counter = 0  # Class / static variable or attribute
    def __init__(self, name, Id):
        self.name = name   # instance variable / attribute
        self.id = Id
        Student.counter += 1

    def details(self):
        print("Name:", self.name, "ID:", self.id, "Student count:", Student.counter)

#============================================================================================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 22)
s3 = Student("Mike", 33)

s3.details()