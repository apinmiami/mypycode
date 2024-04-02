# Methods of array module
import array as arr
# myar=arr.array("i",[10,20])
# n=int(input("Enter the limit for Array: "))
# print("Elements for Array")
# for i in range(n):
#     x=int(input())
#     myar.append(x) # it will add elements in the end
# print(myar)
# myar=arr.array("i",[10,20,30,40,50,90,20,20,30])
# # myar.insert(3,400) # this will insert 400 at 3rd index and 40 will be pushed to 4th index
# print(myar)
# myar.reverse() # This method will reverse the order
# print(myar)
# m=myar.count(20)
# print(m)
# example of searching
# myar=arr.array("i",[])
# n=int(input("Enter the limit for Array: "))
# print("Elements for Array")
# for i in range(n):
#     x=int(input())
#     myar.append(x)
# s=int(input("Enter the number for search  "))
# n=myar.count(s)

# if n > 0:
#     print('Search is successful')
# else:
#     print("NOT FOUND")
# Example of remove method
myar=arr.array("i",[10,20,30,40,50,90,20,20,30,1000])
print(myar)
# print("Before remove",len(myar))
# myar.remove(20)     # it will remove first occurance of 20 and length become short
# print("After remove",len(myar))

# example to find element on particular index
# print(myar.index(20)) # will show index number of first ocuurance of 20

# example of pop methos last in first out LIFO
myar.pop()
print("after pop", myar)

# convert array into list
mylist=myar.tolist()
mylist.append("Anant")
print(mylist)




