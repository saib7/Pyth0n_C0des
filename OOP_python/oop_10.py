# Method overloading :
# If a class has multiple methods having same name but different in parameters, it is known as Method Overloading
# Unlike other programming languages, python does not support it by default.
# But we can achieve it in some way (using decorator)
from multipledispatch import dispatch
class my_calculator:
    @dispatch(int, int)
    def product(self, a, b):
        print(a*b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a*b*c)

    @dispatch(int)
    def product(self, a):
        print(a)

    @dispatch(str, str)
    def product(self, a, b):
        print(int(a)*int(b))


#======================================================================================================================================
    
c1 = my_calculator()

c1.product(4)
c1.product(6,8)
c1.product(6,8,4)
c1.product("6", "9")


# method overloading achieving in python