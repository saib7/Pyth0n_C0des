# Constructor Overloading using **keyargs

class Student:

    def __init__(self, **info):
        if len(info) ==3:
            self.name = info["name"]
            self.Id = info["Id"]
            self.CGPA = info["CGPA"]
        elif len(info) ==2:
            self.name = info["name"]
            self.Id = info["Id"]
        elif len(info) ==1:
            self.name = info["name"]

        print("A student object created.")

#=================================================================================================================================

s1 = Student(name="Carol", Id=33, CGPA=3.91)
s2 = Student(name="Natasha", Id=11, CGPA=3.12)
s3 = Student(name="Mike")
s4 = Student()
