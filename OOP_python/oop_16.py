# Encapsulation -2 (on methods)
class Student:
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id

    def details(self):
        print("Name:", self.name, "ID", self.__id)
        self.__method()


    def __method(self):              # private method (encapsulation)
        print("Private method executed.")

#===================================================================================================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

# s1.__method()
s1.details()
# print(s1.__dict__)

