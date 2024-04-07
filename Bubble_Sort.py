# THIS IS PROGRAM OF BUBBLE SORT or adjuncy arrange technique
#By Anant Panchal
import array as ar
myar=ar.array('i',[])
n=int(input("Enter limit of array: "))
print("Enter Elements is Array: ")
for i in range(n):
    x=int(input())
    myar.append(x)

for i in range(n):
    for j in range(n-i-1):
        if(myar[j]>myar[j+1]):
            temp=myar[j]
            myar[j]=myar[j+1]
            myar[j+1]=temp

print("Sorted Array")
print(myar)
