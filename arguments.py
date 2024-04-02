# understang arguments in function positional argument
# def addition(a,b,c,d):
#    z=a+b+c+d
#    print("Addition is %d" %z)


# calling
#addition(10,20,30,40)
# Default argument
def addition(a,b,c,d=100):
    z=a+b+c+d
    print("Addition is %d" %z)


# calling
# addition(1,2,3) # we didnt give value of d but it too default value
addition(1,2,3,4)# In this we gave the value for d and it replaced the default one