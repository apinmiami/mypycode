# This is example to read data in single line taking input from user
# a,b=input("Enter Two Numbers : ").split(' ')
#print(a+b) # This will concinate the str, bcz input method retuns str as output
# if a =1- and b=20 result of a+b will be 1020 bcz these are str

# Example to read data in single line with type casting and split and map method
# a,b=map(int,input("Enter Two Numbers : ").split(' '))
# print(a+b)

# Example of formating the print statement
# a,b=map(int,input("Enter Two Numbers : ").split(' '))
# c=a+b
# print("Addition of first number %d and second num %d is %d"%(a,b,c))
# print(f"addition of first num {a}and secon num {b}is total {c}", "**" ,a,b,c)

# Example of sepration menthods

# another example of string formating
rno=100; name="Anant"; age=65
str="Roll No is {} Nmae is {} and age is {}"
print(str.format(rno,name,age))
