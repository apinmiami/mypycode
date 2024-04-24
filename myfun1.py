# eXAMPLES TO CALL BY VALUE IN FUNCTION
# def display():
#     print("hi")
#
# #calling of fun
# display() # This will print hi

# # Call by value
### making a function to calculate factorial
# def xyz():
#     a=100 # this is local variable inside fun and it works in the block of func,
#     print(a)
#     print("This id is of variable inside function local")
#     print(id(a))
#     a +=10
#
# def abc():
#     a=500
#     print(a)
#     print("This variable is also local but of abc func id is diffrent")
#     print(id(a))
# #Calling
# xyz()
# abc()
# a=50 # this is calling local variable both are diffrent and diffrent it
# print(a)
# print("This is is local variable in calling place outside func block")
# print(id(a))

# def fact(n): # n is parameter or formal argument, CALLING BY VALUE
#     f=1
#     while n !=0:
#         f=f*n
#         n=n-1
#         print("Factorial is ", f)
# # calling
# c=5
# n=int(input("Enter a number: "))
# print()
# print("this is factorial of value c")
# fact(c) # this is argument we are passing value 5 in c which n will take it to process
# print()
# print("This factorial of number n taken from user: ",n)
# fact(n) # The number of argument and parameter must be equal in number or it will show error

