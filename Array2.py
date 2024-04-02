# code of collection of data in array n limit
import array as arr
myar=arr.array("i",[])
print(len(myar))
n=int(input("Enter the limit "))
print("Enter Elements in array")
for i in range(n):
    x=int(input())
    myar.append(x)
for i in range(n):
    print(myar[i], end=" ")