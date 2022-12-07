# Abstract class and method

from abc import ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def method1(self):
        pass
#======================================================================================================================================
class B(A):
    def method1(self):
        print("Method1 is overridden.")

b = B()
b.method1()
