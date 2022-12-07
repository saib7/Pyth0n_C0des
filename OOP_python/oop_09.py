# method overloading achieving in python
class my_calculator:
    

    # def product(self, num1, num2=None, num3=None):
    #     if num1 != None and num2 != None and num3 != None:
    #         print(num1*num2*num3)
    #     elif num1 != None and num2 != None: 
    #         print(num1*num2)
    #     else:
    #         print(1*num1)

    def product(self, *nums):  # *nums is for accepting unknown number of arguments, it is being accepted as a tuple
        prod = 1
        print(nums)
        for x in nums:
            prod = prod*x
        print(prod)




#======================================================================================================================================
    
c1 = my_calculator()
c1.product(6)
c1.product(6,8)
c1.product(6,8,4)


# method overloading achieving in python