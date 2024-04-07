# THIS IS PROGRAM FOR SEARHING AN ELEMENT IN ARRAY- note array shoud be sorted
# By ANANT Panchal
import array as ar

import numpy as np

n=int(input("Enter the limit: "))
myar=ar.array('i',[])
print("Enter %d elements in array"%n)
for i in range (n):
    x=int(input())
    myar.append(x)
s=int(input("Enter an Element for search: "))
myar1=np.reshape(myar,(n))
myar1.sort()
low=0
high=n-1
f=0
while low<=high:
    mid=(low+high)//2
    if(s==myar1[mid]):
        f=1
        break
    elif(s>myar1[mid]):
        low=mid+1
    else:
        high=mid-1
if f==1:
    print("Searching sucess, element %d is"%s)
else:
    print(f"searching not success, element is {s}")


