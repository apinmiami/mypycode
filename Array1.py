# About Array
import array as arr
# myar=arr.array('b',[10,20,30,50,-9]) #'b' is with signed + 0r - sign numbers
# print(myar)

# myar1=arr.array('B',[10,20,30,50,]) # "B" Unsigned number only +
# print(myar1)

myar2=arr.array("i",[10,100,20,30,40,50]) # this is "i" type takes upto 2 bytes data=16bit= 2**16=655356
#Direct access
for x in myar2:
    print(x, end=" ")

# Access data using index number
# n=len(myar2)
# for i in range(n):
#     print(myar2[i], end=" ")

# Accesing by slicing myar2

# print(myar2[4])
# print(myar2[1:4])
# print(myar2[:4])
# print(myar2[4:])