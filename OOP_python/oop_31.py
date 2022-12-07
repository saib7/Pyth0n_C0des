# Abstract class and method --2

from abc import ABC, abstractclassmethod

class A(ABC):
    @abstractclassmethod
    def method1(self):
        pass
#======================================================================================================================================
class B(A):
    @abstractclassmethod
    def method2(self):
        pass
#======================================================================================================================================
class C(B):

    def method2(self):
        print("Method2 is overridden.")

    def method1(self):
        print("Method1 is overridden.")

c = C()
c.method1()
c.method2()
