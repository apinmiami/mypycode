# This comparison of array using any , where and, all method

import numpy as np
# myar1=np.array([2,4,5,3,6,9])
# myar2=np.array([2,4,5,3,6,9])
# myar3 = myar1 == myar2
# print(myar3)
# if(np.all(myar3)): In this all the elements must be same
#     print("hello")
# else:
#     print("bye")

#example of any method
myar1=np.array([2,10,9,3,6,9])
myar2=np.array([2,4,5,3,6,9])
#myar3 = myar1 == myar2
# myar3= myar1 > myar2
# print(myar3)
# if(np.any(myar3)): # in this if any element is True it prints Hello other wise bye
#     print("hello") # any of the value is TRUE
# else:
#     print("bye")
#
# if(np.all(myar3)):
#     print("Hi")
# else:
#     print("Tata") # bcz all values not true

# eample of WHERE module to create new array using some math condition
newar=np.where(myar1%2==0, myar1,0) # this will make array of even and at odd will put 0
print(newar)
newar1=np.where(myar1>0, myar1, 0)
print(newar1) # this will print all positive mumbers