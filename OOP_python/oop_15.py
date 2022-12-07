# Encapsulation -1 (on attributes)
class Student:
    def __init__(self, name, Id):
        self.name = name
        self.__id = Id  # private instance variable

    def details(self):
        print("Name:", self.name, "ID:", self.__id)

    def set_ID(self, Id):
        if (Id > 0):                                        # getter-setter method
            self.__id = Id
        else:
            print("Invalid ID, enter ID again.")

    def get_ID(self):
        return self.__id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
#=================================================================================================================================

s1 = Student("Bob", 11)
s2 = Student("Carol", 24)

s2.set_ID(14)
print(s2.get_ID())

s1.set_name("Mike")
print(s1.get_name())


s1.details()
s2.details()