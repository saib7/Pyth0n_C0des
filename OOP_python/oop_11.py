# Constructor overloading in Java refers to the use of more than one constructor in an instance class
# Python does not support it but we can achieve it i some way
# Constructor Overloading using *args

class Student:

    def __init__(self, *info):
        if len(info) ==3:
            self.name = info[0]
            self.Id = info[1]
            self.CGPA = info[2]
        elif len(info) ==2:
            self.name = info[0]
            self.Id = info[1]
        elif len(info) ==1:
            self.name = info[0]

        print("A student object created.")

#=================================================================================================================================

s1 = Student("Carol", 33, 3.91)
s2 = Student("Natasha", 11, 3.12)
s3 = Student("Mike")
s4 = Student()
