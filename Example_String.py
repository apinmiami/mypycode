# This are examples of strings
# s=input("Enter a string: ")
# print(type(s)) # will show type of class is str
# print(s.upper()) # will print in all UPPER case
# print(s.lower()) # Will print all in lower case
# s="Anant panchal lives in Miami"
# print(s.count("An")) # will count character or words
# print(s.count("a",4))
# WHAT IS PYTHON STRING?
# A String is a data structure in Python Programming that represents a sequence of characters.
# It is an immutable data type, meaning that once you have created a string,
# you cannot change it.

# A Python string is a sequence of characters. There is a built-in class ‘str’
# for handling Python string.
# You can prove this with the type() function.

# Programming does not have a character data type, a single character is simply a string
# with a length of 1. Let’s see the Python string syntax:

# SYNTAX OF STRING DATA TYPE IN PYTHON
# string_variable = "Hello, world!"
# EXAMPLE:-

# string_0="A Computer Science portal for geeks"
# print(string_0)
# print(type(string_0)) # will show class of string

# 1. Creating  string with singe quote
# str1='Welcome to the geeks world'
# print("Strings with the use of single quotes: ")
# print(str1)

# 2. Creating  string with Double quotes
# str1="I am a geek"
# print("\nString with the use of Double quotes: ")
# print(str1)

# 3. Creating  string with Triple quotes
# str1='''Geeks
#      for
#      Life'''
# print("\nCreating a multiline string: ")
# print(str1)

# 4. Python Program to Access
# characters of String
# str1="GeeksforGeeks"
# print("Initial string: ")
# print(str1)
# print("\n First character of strind is : ")
# print(str1[0])
# print("\nLast character of string is : ")
# print(str1[-1])

# 5. A string is immutable it cant be changed
# EXAMPLE:-
# a="Dogs"
# a[0]="H"
# print(a) # will show error ( TypeError: 'str' object does not support item assignment)

# 6. Slicing Of String
# Examples:-
# str1="Anant panchal Lives in Miami"
# print("Initial String")
# print(str1)
# # Printing 3rd to 12th character
# print(len(str1))
# print("\nSlicing character from 3 to 12: ")
# print(str1[3:12])
# print("\nSlice to get Anant panchal: ")
# print(str1[0:13])
# # Printing character between 3rd and 2nd last character
# print("\n slice between 3rd and 2nd last character: ")
# print(str1[3:-2])
# print(str1.find("M")) # This will show index number of character which is 23
# # slice from 23 to end of the string result should come Miami
# print("\n slicing from 23 to get Miami: ")
# print(str1[23:])
# print(str1[-3:-2])  #This prints characters from three characters from the string’s end to two characters from it.
# print(str1[-2:-2]) # will result empty string

# 7.  Reversing a python string
# EXAMPLES:-
# str1="GeeksforGeeks"
# print(str1[::-1])
#
# # We can also reverse a string by using built-in join and reversed functions, and passing the string as the parameter
# # to the reversed() function.
# str1="".join(reversed(str1))
# print(str1)

# 8.  Python String Concatenation
# Examples:-
a="Do you see this"
b="$$?"
c=a+b
print(c)

x='10'
# print(2*x) # Multiplying ‘a’ by 2 returned 1010, and not 20, because ‘10’
# is a string, not a number. You cannot concatenate a string to a number.

# m="10"
# n=10
# p=m+n
# print(p) # will throw error (TypeError: can only concatenate str (not "int") to str)