# Multiple inheritance
class A:
    def __init__(self):
        print("__init__ of class A")

    def method1(self):
        print("Method1 of class A")
#=====================================================================================================================================
class B:
    def __init__(self):
        print("__init__ of class B")

    def method1(self):
        print("Method1 of class B")
#=====================================================================================================================================
class C(A,B):   # order matters
    def __init__(self):
        # super.__init__()
        # B.__init__(self)   # Calling as a reference of class B
        print("__init__ of class C")

    def method2(self):
        print("Method2 of class C")
#=====================================================================================================================================

c1 = C()
c1.method1()
c1.method2()

B.method1(c1) # for specifically calling method1 from class B

# program will always follow Method Resulation Order (A->B)
