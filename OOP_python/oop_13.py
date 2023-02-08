# Operator Overloading 1
# Polymorphism: Polymorphism (or operator overloading) is a manner in which OO systems allow the same operator name or symbol to be used for multiple operations. That is, it allows the operator symbol or name to be bound to more than one
# watch this video for more detail: https://www.youtube.com/watch?v=L2vovuEndXY&list=PLvr0Ht-XkB_3NAwjutgaG0-62d2yjG6qz&index=18


class data:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x
    

#====================================================================================================================================

num1 = data(10)
num2 = data(20)
str1 = data("cse")
str2 = data("111")
print(num1+num2) # num1.__add__(num2)
print(str1+str2)